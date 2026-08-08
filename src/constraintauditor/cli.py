"""CLI: constraint-auditor audit|check-constraints|parse-transcript."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .audit import run_audit, write_report
from .journal import parse_loop_engine_journal
from .spec import SpecError, load_constraint_spec


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="constraint-auditor")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_audit = sub.add_parser("audit", help="audit transcript against constraints")
    p_audit.add_argument("--constraints", required=True)
    p_audit.add_argument("--transcript", required=True)
    p_audit.add_argument("--format", default="auto", choices=["auto", "journal", "jsonl"])
    p_audit.add_argument("--report", default=None)
    p_audit.add_argument("--json", action="store_true")

    p_check = sub.add_parser("check-constraints", help="validate constraint spec only")
    p_check.add_argument("path")

    p_parse = sub.add_parser("parse-transcript", help="dry-run journal parser")
    p_parse.add_argument("path")

    args = parser.parse_args(argv)

    try:
        if args.cmd == "check-constraints":
            spec = load_constraint_spec(args.path)
            print(f"OK: {spec.name} ({len(spec.constraints)} constraints)")
            return 0
        if args.cmd == "parse-transcript":
            events = parse_loop_engine_journal(args.path)
            print(f"OK: {len(events)} events")
            for e in events:
                print(f"- {e.timestamp}: {list(e.fields.keys())}")
            return 0
        if args.cmd == "audit":
            if not Path(args.constraints).exists() or not Path(args.transcript).exists():
                print("ERROR: missing constraints or transcript path", file=sys.stderr)
                return 1
            result = run_audit(args.constraints, args.transcript, fmt=args.format)
            if args.report:
                write_report(result, args.report)
            if args.json:
                print(json.dumps(result.to_jsonable(), indent=2))
            else:
                print(
                    f"verdict={result.verdict} exit={result.exit_code} "
                    f"violations={result.decay.n_violations} "
                    f"first_index={result.decay.first_violation_index} "
                    f"slope={result.decay.decay_slope:.3f}"
                )
            return result.exit_code
    except SpecError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
