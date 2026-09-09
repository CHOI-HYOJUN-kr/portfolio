"""Verify recorded benchmarks and rejection of corrupted publication data."""
import csv
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from verify_metrics import DATA, verify


class MetricIntegrityTests(unittest.TestCase):
    def test_reported_benchmarks(self):
        actual = {name: value for name, value, _ in verify()}
        for name, expected in {"Case A": 1385.109561, "Case B": 0.682053,
                               "Case C": 5.662205, "Reported ML": 0.558965}.items():
            self.assertAlmostEqual(actual[name], expected, places=6)

    def test_corrupt_publication_rejected(self):
        with DATA.open(encoding="utf-8", newline="") as source:
            reader = csv.DictReader(source)
            rows, fields = list(reader), reader.fieldnames
        for corruption in ("changed_J", "nan", "missing_case", "wrong_unit", "negative"):
            with self.subTest(corruption=corruption), tempfile.TemporaryDirectory() as temp:
                changed = [dict(row) for row in rows]
                if corruption == "changed_J": changed[0]["J_reported"] = "0"
                elif corruption == "nan": changed[0]["curveRMS"] = "NaN"
                elif corruption == "wrong_unit": changed[1]["curveRMS"] = "3.681075"
                elif corruption == "negative": changed[1]["curveRMS"] = "-0.003681075"
                else: changed.pop()
                path = Path(temp)/"changed.csv"
                with path.open("w", encoding="utf-8", newline="") as dest:
                    writer = csv.DictWriter(dest, fieldnames=fields)
                    writer.writeheader(); writer.writerows(changed)
                with self.assertRaises(ValueError): verify(path)


if __name__ == "__main__": unittest.main()
