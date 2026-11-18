---
name: run-round
description: Run one round of the workflow. Picks the next item from data/items.csv, has the scout research it, the writer draft it and the reviewer check it. Use when the user types /run-round.
---

# /run-round

1. Read `docs/guide.md`, section "Selection rules" only (Grep the heading, Read with offset).
2. Pick the next item from `data/items.csv`. Tell the user which one.
3. Call the `scout` agent with the item id. It returns confirmed facts with sources.
4. Call the `writer` agent with those facts and the "Draft template" section.
5. Call the `reviewer` agent on the draft. If it fails, fix once and re-check.
6. Save the draft to `out/<id>.md`, set status to `drafted`, and show the draft.
7. Stop. A human sends it. Never send anything yourself.

Run independent calls in the same message to save context.
