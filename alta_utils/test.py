import unittest
import sys

class EmailingCase(unittest.TestCase):
    def test_error_email(self):
        from logger import Logger
        lggr = Logger(
            sender_email='targo.support@arcpet.co.uk',
            info_email='henryt@arcpet.co.uk',
            error_email='henryt@arcpet.co.uk',
            production_db_server='ArcSql',
            internal_domain='Arcpet'
        )
        lggr.send_error_email(__name__, 'test', f"Testing")