---
name: log-sent
description: Record that a human sent a draft, with the variant used. Use when the user types /log-sent <id> [variant] or says "sent I001".
---

# /log-sent

Arguments: item id, optional variant (A, B, ...).

1. Check the item exists in `data/items.csv`; if not, say so and stop.
2. Set `status=sent`, `date=<today, ISO>` and `variant=<variant>` with a minimal edit of that row.
3. Confirm in one line what changed. Do not touch other rows.
