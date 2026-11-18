import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))
import install  # noqa: E402


def test_creates_then_is_idempotent(tmp_path):
    first = install.install(tmp_path)
    assert set(first.values()) == {"created"}
    assert (tmp_path / ".claude" / "skills" / "run-round" / "SKILL.md").exists()
    second = install.install(tmp_path)
    assert set(second.values()) == {"unchanged"}


def test_keeps_modified_files_unless_forced(tmp_path):
    install.install(tmp_path)
    f = tmp_path / "CLAUDE.md"
    f.write_text("my own rules")
    assert install.install(tmp_path)["CLAUDE.md"] == "kept"
    assert f.read_text() == "my own rules"
    assert install.install(tmp_path, force=True)["CLAUDE.md"] == "replaced"
    assert (tmp_path / "CLAUDE.md.bak").read_text() == "my own rules"


def test_dry_run_writes_nothing(tmp_path):
    install.install(tmp_path, dry_run=True)
    assert not any(tmp_path.iterdir())


def test_every_skill_and_agent_has_frontmatter():
    root = pathlib.Path(install.TEMPLATE) / ".claude"
    for f in list(root.rglob("SKILL.md")) + list((root / "agents").glob("*.md")):
        text = f.read_text(encoding="utf-8")
        assert text.startswith("---\nname:") and "description:" in text.split("---")[1], f
