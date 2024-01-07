from unittest import TestCase

from ttvn.parse import Parser

class TestParser(TestCase):

    def setUp(self):
        self.parser = Parser()

    def test_parse_case_1(self):
        from tests.fixtures.parser import TEST_CASES
        for INPUT, EXPECTED in TEST_CASES:
            self.parser.parse_text(INPUT)
            ACTUAL = self.parser.parsed
            self.assertEqual(ACTUAL, EXPECTED)
