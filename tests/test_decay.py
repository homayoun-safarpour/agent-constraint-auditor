from constraintauditor.checkers import Violation
from constraintauditor.decay import compute_decay


def test_quartile_violation_rate():
    # 8 events, violations in last half
    violations = [
        Violation("c", 4, "t", "d"),
        Violation("c", 5, "t", "d"),
        Violation("c", 6, "t", "d"),
        Violation("c", 7, "t", "d"),
    ]
    decay = compute_decay(8, violations)
    assert decay.quartile_rates[0] == 0.0
    assert decay.quartile_rates[3] > 0.0


def test_first_violation_index():
    violations = [Violation("c", 3, "t", "d"), Violation("c", 5, "t", "d")]
    decay = compute_decay(8, violations)
    assert decay.first_violation_index == 3


def test_decay_slope_detects_increase():
    violations = [Violation("c", i, "t", "d") for i in (6, 7)]
    decay = compute_decay(8, violations)
    assert decay.decay_slope > 0
