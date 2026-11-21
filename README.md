# tiny-chess-v3

A tiny chess engine in at most 4,096 bytes of Python, written for the
[make.fun tiny-chess-01 bounty](https://make.fun/bounty/tiny-chess-01).

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/zairzuab/tiny-chess-v3/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/zairzuab/tiny-chess-v3/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

## Engine

`main.py` (4,085 bytes) is the whole engine: a 0x88 board, alpha-beta search
with quiescence and iterative deepening on a fixed node budget (50,000
nodes a move, never a clock), MVV-LVA move ordering, and an evaluation of
material plus centralisation and pawn advancement. It talks to the trial
environment over HTTP (`MAKEFUN_ENV_URL`), plays its moves in UCI, and is
fully deterministic, so a replay plays the same moves.

## Layout

- `main.py` — the engine (the only file the trial runs)
- `README.md` — this file
- `LICENSE` — MIT
