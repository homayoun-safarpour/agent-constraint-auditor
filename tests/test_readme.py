from pathlib import Path

from constraintauditor.cli import main

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8-sig")
DECAYING_CONSTRAINTS = str(ROOT / "examples" / "decaying" / "constraints.yaml")
DECAYING_JOURNAL = str(ROOT / "examples" / "decaying" / "journal.md")
STABLE_CONSTRAINTS = str(ROOT / "examples" / "stable" / "constraints.yaml")
STABLE_JOURNAL = str(ROOT / "examples" / "stable" / "journal.md")
FIRST_SCREEN_COMMAND = (
    "constraint-auditor audit --constraints examples/decaying/constraints.yaml "
    "--transcript examples/decaying/journal.md"
)
FIRST_SCREEN_OUTPUT = "verdict=DECAY exit=2 violations=3 first_index=2 slope=2.000"


def test_readme_spoken_h1_is_constraint_auditor_first_line():
    assert README.splitlines()[0] == "# constraint-auditor"


def test_readme_first_screen_locks_clone_install_command_and_output():
    head = "\n".join(README.splitlines()[:22])
    assert "git clone https://github.com/homayoun-safarpour/agent-constraint-auditor" in head
    assert "cd agent-constraint-auditor && pip install -e ." in head
    assert FIRST_SCREEN_COMMAND in head
    assert FIRST_SCREEN_OUTPUT in head
    assert "Interview pack" not in head
    assert "verdict=CLEAN" not in head
    assert "\u2014" not in head


def test_readme_install_comes_before_problem_and_interview_pack():
    pip_at = README.find("pip install -e .")
    assert 0 <= pip_at < README.find("## The problem")
    assert 0 <= pip_at < README.find("## What each result means")
    assert 0 <= pip_at < README.find("Interview pack")


def test_readme_opening_paragraph_sits_before_clone():
    clone_at = README.find("git clone")
    opening = [
        line
        for line in README[:clone_at].splitlines()
        if line.startswith("constraint-auditor is ")
    ]
    assert len(opening) == 1
    words = len(opening[0].split())
    assert 70 <= words <= 110, words
    assert "We built it because" in opening[0]


def test_readme_has_no_em_dash():
    assert "\u2014" not in README


def test_readme_first_screen_output_is_real(capsys):
    code = main(
        ["audit", "--constraints", DECAYING_CONSTRAINTS, "--transcript", DECAYING_JOURNAL]
    )
    assert code == 2
    assert capsys.readouterr().out.strip() == FIRST_SCREEN_OUTPUT
    assert "That command exits 2." in README


def test_readme_stable_twin_exits_0():
    code = main(["audit", "--constraints", STABLE_CONSTRAINTS, "--transcript", STABLE_JOURNAL])
    assert code == 0
    assert "The same audit on `examples/stable/` exits 0." in README
