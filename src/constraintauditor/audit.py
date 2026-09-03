"""Run a full audit: load spec + transcript, check, score decay."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from pathlib import Path

from .checkers import Violation, check_transcript
from .decay import DecayReport, compute_decay, markdown_timeline
from .journal import TranscriptError, detect_format, parse_loop_engine_journal
from .spec import ConstraintSpec, load_constraint_spec


@dataclass
class AuditResult:
    verdict: str  # CLEAN | DECAY
    exit_code: int
    spec_name: str
    decay: DecayReport
    violations: list[Violation]

    def to_jsonable(self) -> dict:
        return {
            "verdict": self.verdict,
            "exit_code": self.exit_code,
            "spec_name": self.spec_name,
            "decay": asdict(self.decay),
            "violations": [asdict(v) for v in self.violations],
        }


def run_audit(
    constraints_path: str | Path,
    transcript_path: str | Path,
    fmt: str = "auto",
) -> AuditResult:
    spec: ConstraintSpec = load_constraint_spec(constraints_path)
    if fmt == "auto":
        fmt = detect_format(transcript_path)
    if fmt not in {"journal", "auto"}:
        # v0.1: journal only
        events = parse_loop_engine_journal(transcript_path)
    else:
        events = parse_loop_engine_journal(transcript_path)
    if not events:
        raise TranscriptError("transcript contains no parseable events")
    violations = check_transcript(spec, events)
    decay = compute_decay(len(events), violations)
    if violations:
        return AuditResult(
            verdict="DECAY",
            exit_code=2,
            spec_name=spec.name,
            decay=decay,
            violations=violations,
        )
    return AuditResult(
        verdict="CLEAN",
        exit_code=0,
        spec_name=spec.name,
        decay=decay,
        violations=[],
    )


def write_report(result: AuditResult, path: str | Path) -> None:
    Path(path).write_text(
        markdown_timeline(result.spec_name, result.decay, result.violations),
        encoding="utf-8",
    )
