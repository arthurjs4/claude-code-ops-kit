"""Idempotent installer: copy the template (skills, agents, per-folder rules, example data) into a target project.

  python scripts/install.py /path/to/project [--force] [--dry-run]

- A file that does not exist is created.
- A file that already matches is left alone ("unchanged").
- A file that exists and differs is NOT overwritten ("kept"), unless --force; with --force the old file is saved
  next to it as <name>.bak first.
Running it twice in a row changes nothing the second time.
"""
import argparse
import pathlib
import shutil
import sys

TEMPLATE = pathlib.Path(__file__).resolve().parents[1] / "template"


def install(target, force=False, dry_run=False):
    """Return a dict {relative_path: 'created' | 'unchanged' | 'kept' | 'replaced'}."""
    target = pathlib.Path(target)
    report = {}
    for src in sorted(p for p in TEMPLATE.rglob("*") if p.is_file()):
        rel = src.relative_to(TEMPLATE)
        dst = target / rel
        if not dst.exists():
            state = "created"
        elif dst.read_bytes() == src.read_bytes():
            state = "unchanged"
        elif force:
            state = "replaced"
        else:
            state = "kept"
        report[rel.as_posix()] = state
        if dry_run or state in ("unchanged", "kept"):
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        if state == "replaced":
            shutil.copy2(dst, dst.with_name(dst.name + ".bak"))
        shutil.copy2(src, dst)
    return report


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)
    for rel, state in install(a.target, a.force, a.dry_run).items():
        print(f"{state:10} {rel}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
