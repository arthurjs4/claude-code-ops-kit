---
name: reply
description: Handle an answer that came back for an item. Saves the conversation and drafts the next message. Use when the user types /reply <id> and pastes the answer.
---

# /reply

1. Append the pasted answer to `out/<id>.conversation.md` with the date.
2. Classify it: yes, no, question, objection, other.
3. Draft the next message (short, one question) using the full conversation as context.
4. Set `status=replied` on the item. Show the draft; a human sends it.
