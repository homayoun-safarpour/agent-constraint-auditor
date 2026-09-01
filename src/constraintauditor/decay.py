"""Decay metrics over a violation stream."""

from __future__ import annotations

from dataclasses import dataclass

from .checkers import Violation


@dataclass(frozen=True)
class DecayReport:
    n_events: int
    n_violations: int
    first_violation_index: int | None
    quartile_rates: tuple[float, float, float, float]
    decay_slope: float


def _quartile_index(i: int, n: int) -> int:
    if n <= 0:
        return 0
    # 0..3
    return min(3, (i * 4) // n)


def compute_decay(n_events: int, violations: list[Violation]) -> DecayReport:
    first = min((v.event_index for v in violations), default=None)
    counts = [0, 0, 0, 0]
    sizes = [0, 0, 0, 0]
    for i in range(n_events):
        q = _quartile_index(i, n_events)
        sizes[q] += 1
    for v in violations:
        q = _quartile_index(v.event_index, n_events)
        counts[q] += 1
    rates = tuple(
        (counts[q] / sizes[q] if sizes[q] else 0.0) for q in range(4)
    )
    # simple slope: last quartile rate - first quartile rate
    slope = rates[3] - rates[0]
    return DecayReport(
        n_events=n_events,
        n_violations=len(violations),
        first_violation_index=first,
        quartile_rates=rates,  # type: ignore[arg-type]
        decay_slope=slope,
    )


def _verdict_sentence(decay: DecayReport) -> tuple[str, str]:
    if decay.n_violations:
        noun = "violation" if decay.n_violations == 1 else "violations"
        return (
            "DECAY",
            (
                f"The transcript records {decay.n_violations} constraint {noun}, "
                f"first at event {decay.first_violation_index}."
            ),
        )
    return (
        "CLEAN",
        f"The transcript holds all declared constraints across {decay.n_events} events.",
    )


def markdown_timeline(spec_name: str, decay: DecayReport, violations: list[Violation]) -> str:
    verdict, sentence = _verdict_sentence(decay)
    lines = [
        f"# Constraint decay report: {spec_name}",
        "",
        f"Verdict: {verdict}",
        sentence,
        "",
        f"Events: {decay.n_events} · Violations: {decay.n_violations}",
        f"First violation index: {decay.first_violation_index}",
        f"Decay slope (Q4-Q1 rate): {decay.decay_slope:.3f}",
        "",
        "## Quartile violation rates",
        "",
        "| Q1 | Q2 | Q3 | Q4 |",
        "| --- | --- | --- | --- |",
        "| "
        + " | ".join(f"{r:.2f}" for r in decay.quartile_rates)
        + " |",
        "",
        "## Violations",
        "",
    ]
    if not violations:
        lines.append("None.")
    else:
        for v in violations:
            lines.append(
                f"- [{v.timestamp}] event {v.event_index} · `{v.constraint_id}` · {v.detail}"
            )
    lines.append("")
    return "\n".join(lines)
