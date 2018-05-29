from unittest import TestCase

from aspLog import ASPLog


class TestASPLog(TestCase):

    def setUp(self):
        self.aspLog = ASPLog()
        self.aspLog.parselog("tests/auto_processed.log")
        print "first line: "+self.aspLog.lines[0]

    def test_parselog(self):
        self.assertEqual(len(self.aspLog.lines), 31)

    def test_encryption(self):
        key = "000102030405060708090a0b0c0d0e0f"  # 16 byte key for AES 128
        encryptedLog = self.aspLog.encrypt(key)
        decryptedLog = self.aspLog.decrypt(encryptedLog, key)
        self.assertEqual(len(decryptedLog), 31)
        print "decrypted: "+decryptedLog[0]

