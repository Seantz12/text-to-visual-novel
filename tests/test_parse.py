from unittest import TestCase

from ttvn.parse import Parser

class TestParser(TestCase):

    maxDiff = None

    def setUp(self):
        self.parser = Parser()

    def test_parser(self):
        from tests.fixtures.parser import TEST_CASES
        for test_case in TEST_CASES:
            INPUT, EXPECTED = test_case
            self.parser.parse_text(INPUT)
            ACTUAL = self.parser.parsed
            self.assertEqual(ACTUAL, EXPECTED)