from unittest import TestCase

from aspLog import ASPLog


class TestASPLog(TestCase):
    def test_parselog(self):
        aspLog = ASPLog()
        lines = aspLog.parselog("tests/auto_processed.log")
        self.assertEqual(len(lines), 31)
        print lines[0]

