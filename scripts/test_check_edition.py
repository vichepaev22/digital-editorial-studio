"""Smoke tests for the static checker. Run: python3 -m unittest discover -s scripts."""
import tempfile
import unittest
from pathlib import Path
from check_edition import check

class CheckerTests(unittest.TestCase):
    def test_starter(self):
        root = Path(__file__).resolve().parent.parent
        self.assertEqual(check(root / "assets/edition-starter.html"), [])

    def test_detects_known_failures(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "broken.html"
            path.write_text('<html><h1>x</h1><div id="a"></div><div id="a"></div><a href="#missing">link</a><img src="missing.png"></html>', encoding="utf-8")
            errors = check(path)
            self.assertEqual(len(errors), 6)
            self.assertIn("Duplicate id: a", errors)
            self.assertIn("Broken static fragment: missing", errors)
            self.assertIn("Missing local asset: missing.png", errors)

if __name__ == "__main__":
    unittest.main()
