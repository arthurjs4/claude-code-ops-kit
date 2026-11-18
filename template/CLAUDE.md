# Project operating rules (example)

This file is loaded by Claude Code at the start of every session. Keep it short; put detail in per-folder `CLAUDE.md` files and in skills.

## How work flows

1. `/run-round` runs one unit of work: pick an item, delegate research to the `scout` agent, draft with the `writer` agent, check with the `reviewer` agent.
2. A human sends or approves anything that leaves the machine. Agents never send, post or pay.
3. `/log-sent` records what the human did. `/reply` handles an answer that came back.

## Global rules

- Facts need a source. If a fact is not confirmed, say "unconfirmed" and leave it out of any output.
- Use `Grep` plus `Read` with offsets instead of reading whole files; keep context small.
- Never put secrets, personal data or real names in files that are committed. Examples in this repo are fictional.
- Per-folder rules live in `data/CLAUDE.md` and `docs/CLAUDE.md`; Claude Code reads them when working in those folders.
