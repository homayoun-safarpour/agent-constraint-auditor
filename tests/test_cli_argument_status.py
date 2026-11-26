import pytest

from constraintauditor.cli import main


@pytest.mark.parametrize("args", [[], ["unknown"], ["audit"], ["audit", "--unknown"]])
def test_bad_arguments_use_error_status(args, capsys):
    with pytest.raises(SystemExit) as exc:
        main(args)
    assert exc.value.code == 1
    assert "usage:" in capsys.readouterr().err


def test_help_retains_success_status():
    with pytest.raises(SystemExit) as exc:
        main(["audit", "--help"])
    assert exc.value.code == 0
