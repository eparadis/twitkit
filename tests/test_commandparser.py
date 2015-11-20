import unittest
from commandparser import commandparser


class CommandParserTests(unittest.TestCase):
    def setUp(self):
        self.testobj = commandparser.CommandParser('foo')

    def test_canParse_doesntmatch(self):
        result = self.testobj.can_parse('notfoo')
        self.assertFalse(result)

    def test_canParse_matches(self):
        result = self.testobj.can_parse('foo')
        self.assertTrue(result)

    def test_firstArgument(self):
        result = commandparser.CommandParser.first_arg('foo bar baz')
        self.assertEqual(result, 'bar')
