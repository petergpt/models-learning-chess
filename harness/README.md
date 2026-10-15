# Repeat the experiment

Use your own agent tools. This folder supplies the experiment structure, prompts, fixed opponent configuration, chess referee, practice interface, rating code, and original referee tests. It does not supply Claude Code or Codex.

The pinned engine setup requires **Python 3.11+ and Linux x86-64**, with internet access for the first setup. No pip installation is needed.

From the repository root:

```sh
python3 harness/new_run.py --model YOUR_MODEL --output runs/my-model
cd runs/my-model
./play verify
```

Setup installs the pinned chess-rule library and downloads the checksum-verified Stockfish 19 opponent. It creates an empty learning workspace and a fresh ledger, and refuses to overwrite an existing run. If you already have the exact engine binary, pass `--engine /path/to/stockfish` to avoid downloading it.

Open your agent in that new run directory and give it this instruction:

> Read AGENTS.md and GOAL.md. Carry out this independent chess-learning experiment. Choose your own learning methods and keep your notes in workspace/. Return periodically to the fixed benchmarks. Stop after 200 scored benchmark games and report the measured results honestly.

The agent needs shell and file tools, its own persistent conversation, and permission to run `./play`. Keep each model’s run separate. Do not expose other runs, this released dataset, spectator engine evaluations, or opponent notes to a learner.

The interface is small:

```sh
./play start
./play board
./play move e2e4
./play status
./play practice start --skill 3 --color white
./play practice move e2e4
./play practice end --note 'Reason for ending the drill'
```

Benchmark games rotate through maximum skill, skill 0, and nominal Elo 1800, with paired colors. The opponent uses **1,000,000 nodes per reply**, **one thread**, **64 MiB hash**, and a fresh engine process for each reply. Three illegal submissions on a turn forfeit. Recorded practice never changes benchmark scores or Elo. Finish an active benchmark before starting practice.

The learner chooses every move and its curriculum. Engine analysis, automated move selection, other-model chess advice, and cross-run information are prohibited. Mechanical board rendering and legality checking are allowed. The full rules are in the generated `AGENTS.md` and `GOAL.md`.

Record the exact model, agent-tool version, effort, context configuration, compaction behavior, starting instructions, and any later interventions. `run-metadata.example.json` is a starting template. Original run instructions and revisions are in `../provenance/`.

There is no learning-token cap. Host and provider limits still apply. Set `CHESS_JOB_RUNNER` to a host job launcher when needed; the play script automatically uses a local `~/.local/bin/t3-job` installation. `--games` and `--nodes` allow small setup checks, which are labeled as a custom-budget protocol.

This setup preserves the referee rules, not the original T3 continuation implementation. Session management and resumption belong to your chosen agent tools. For a head-to-head follow-up, retain each completed learner’s own conversation and notes; the original match started from native post-200 branches, not just final notes. New runs can differ because model services, context management, and weakened-engine randomness can change.
