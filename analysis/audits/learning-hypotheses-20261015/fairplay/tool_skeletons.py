#!/usr/bin/env python3
"""Minimize authored notes while preserving executable shell/Python for review."""
import io
import json
from pathlib import Path
import re
import tokenize

OUT = Path(__file__).resolve().parent
calls = json.loads((OUT / 'fable-nonroutine-tool-calls.json').read_text())


def compact_python(source):
    try:
        toks = []
        for tok in tokenize.generate_tokens(io.StringIO(source).readline):
            if tok.type == tokenize.STRING and len(tok.string) > 250:
                tok = tok._replace(string=repr('<authored string %d characters>' % len(tok.string)))
            toks.append(tok)
        return tokenize.untokenize(toks)
    except (tokenize.TokenError, IndentationError):
        return source


def skeleton(source):
    lines = source.splitlines()
    out, i = [], 0
    while i < len(lines):
        line = lines[i]
        match = re.search(r'<<\s*[-]?\s*[\x27\"]?([A-Za-z_][A-Za-z_0-9]*)', line)
        out.append(line)
        i += 1
        if match:
            body = []
            delim = match.group(1)
            while i < len(lines) and lines[i].strip() != delim:
                body.append(lines[i]); i += 1
            text = '\n'.join(body)
            if re.search(r'python\d?\b', line):
                out.append(compact_python(text))
            else:
                out.append('<authored heredoc: %d lines, %d characters>' % (len(body), len(text)))
            if i < len(lines):
                out.append(lines[i]); i += 1
    return '\n'.join(out)


result = []
for call in calls:
    entry = {k: v for k, v in call.items() if k != 'command'}
    if 'command' in call:
        entry['skeleton'] = skeleton(call['command'])
    result.append(entry)
(OUT / 'fable-execution-skeletons.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({'calls': len(result), 'file': str(OUT / 'fable-execution-skeletons.json')}))
