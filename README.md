# claude-code-ops-kit

A small, generic template for running a repeatable workflow inside **Claude Code**: skills as slash commands, specialised subagents, per-folder rules, and an idempotent installer.

## Why

Once a workflow repeats (research an item, draft something, have a human send it, log what happened), prompts pasted into chat drift. Claude Code gives you three building blocks that keep the workflow stable:

- **Skills as commands** (`.claude/skills/<name>/SKILL.md`): `/run-round`, `/log-sent`, `/reply` here. Each is a short, numbered procedure.
- **Specialised agents** (`.claude/agents/*.md`): `scout` (read-only research), `writer` (drafts), `reviewer` (checks without editing). Each has a minimal tool list.
- **Rules per folder** (`CLAUDE.md` in `data/` and `docs/`): loaded when Claude works in that folder, so global context stays small.

Design principles baked into the examples: facts need sources; agents never send, post or pay (a human does); read with `Grep` plus offsets; delegate and run independent calls together.

The content is intentionally a toy workflow with fictional data. Replace the skills, agents and guide with your own.

## Install

```bash
python scripts/install.py /path/to/your/project --dry-run   # see what would happen
python scripts/install.py /path/to/your/project             # copy the template in
```

The installer is **idempotent**: new files are created, identical files are left alone, and files you changed are kept (use `--force` to replace; the old file is saved as `.bak`). Run it twice and the second run changes nothing.

## Usage

Open the target project in Claude Code and type `/run-round`, `/log-sent I002 A` or `/reply I003`.

## Example output

```
$ python scripts/install.py ./my-project
created    .claude/agents/reviewer.md
created    .claude/agents/scout.md
created    .claude/agents/writer.md
created    .claude/skills/log-sent/SKILL.md
...
$ python scripts/install.py ./my-project
unchanged  .claude/agents/reviewer.md
...
```

## Layout

```
template/
  CLAUDE.md                      global rules
  .claude/skills/{run-round,log-sent,reply}/SKILL.md
  .claude/agents/{scout,writer,reviewer}.md
  data/CLAUDE.md, data/items.csv per-folder rules and fictional data
  docs/CLAUDE.md, docs/guide.md
scripts/install.py
```

## Tests

```bash
pip install pytest && pytest
```

## Limitations

- Skill and agent file formats are those of Claude Code today and may change.
- The workflow is an illustration, not a product. `out/` is created by the skills at run time.
- The installer copies files only; it does not merge changes into files you edited.

## License

MIT

## Resumo em português

Modelo genérico de operação no Claude Code: skills como comandos (`/run-round`, `/log-sent`, `/reply`), agentes especializados (pesquisa, redação, revisão) e regras por pasta. Inclui um instalador idempotente: cria o que falta, não mexe no que já é igual e preserva o que você alterou (use `--force` para substituir, com cópia `.bak`). Todo o conteúdo é de exemplo, com dados fictícios.
