#!/usr/bin/env python3
"""Recalculate stored J values; does not run a vehicle model or an RF model.

Added with Codex for the September 2026 portfolio. The rule is transcribed
from the project report / LKSUtils.calcCost. Missing/non-finite values are
rejected here rather than assigned the legacy simulation fallback penalty.
"""
import argparse
import csv
import math
from pathlib import Path
import sys

RULES = {
    "under": (0.10, 0.05),
    "curveRMS": (0.01, 0.45),
    "curveBIAS": (0.005, 0.20),
    "settle10": (3.0, 0.08),
    "dfmax": (3.0, 0.07),
    "dfrate": (5.0, 0.03),
    "yawmax": (15.0, 0.04),
    "aymax": (4.0, 0.10),
}
EXPECTED_CASES = {"Case A", "Case B", "Case C", "Reported ML"}
DATA = Path(__file__).resolve().parents[1] / "data/reported_metrics.csv"


def calculate_cost(metrics):
    for field in RULES:
        if not math.isfinite(metrics[field]) or metrics[field] < 0:
            raise ValueError(f"{field} must be a finite non-negative value")
    total = sum(metrics[field] / reference * weight for field, (reference, weight) in RULES.items())
    if metrics["dfmax"] > 3:
        total += 0.25 * (metrics["dfmax"] / 3 - 1) ** 2
    if metrics["dfmax"] > 5.5:
        total += 100
    if metrics["curveRMS"] > 0.015:
        total += 5 * (metrics["curveRMS"] / 0.015 - 1) ** 2
    if metrics["curveBIAS"] > 0.005:
        total += 5 * (metrics["curveBIAS"] / 0.005 - 1) ** 2
    if not math.isfinite(total):
        raise ValueError("Cost overflow")
    return total


def verify(path=DATA):
    with Path(path).open(encoding="utf-8-sig", newline="") as source:
        rows = list(csv.DictReader(source))
    cases = [row["case"] for row in rows]
    if len(cases) != 4 or set(cases) != EXPECTED_CASES:
        raise ValueError("Expected exactly one row for A, B, C and Reported ML")
    results = []
    for row in rows:
        metrics = {field: float(row[field]) for field in RULES}
        expected = float(row["J_reported"])
        actual = calculate_cost(metrics)
        if not math.isfinite(expected) or not math.isclose(actual, expected, abs_tol=1e-6, rel_tol=0):
            raise ValueError(f"{row['case']}: J mismatch, saved={expected}, recalculated={actual}")
        results.append((row["case"], actual, abs(actual - expected)))
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, default=DATA)
    args = parser.parse_args()
    try:
        for name, value, difference in verify(args.csv):
            print(f"{name:12} J={value:.9f} | difference={difference:.3g}")
        print("PASS: 4 stored metric rows agree with the published cost rule.")
        print("This is arithmetic verification, not simulation or hardware reproduction.")
        return 0
    except (ValueError, KeyError, TypeError, OSError, OverflowError, csv.Error) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
