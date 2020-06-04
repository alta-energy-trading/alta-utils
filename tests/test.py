import unittest
import sys
sys.path.append('../')


class LoggingCase(unittest.TestCase):
    def test_logging_imports_ok(self):
        import alta_utils.alta_logging


class EmailingCase(unittest.TestCase):
    def test_emailing_imports_ok(self):
        import alta_utils.alta_emailing