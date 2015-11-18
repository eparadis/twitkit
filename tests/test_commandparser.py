import unittest
from commandparser import commandparser

class CommandParserTests( unittest.TestCase):

  def setUp(self):
    self.testobj = commandparser.CommandParser('foo')

  def test_canParse_doesntmatch(self):
    result = self.testobj.canParse('notfoo')
    self.assertFalse(result)
  
  def test_canParse_matches(self):
    result = self.testobj.canParse('foo')
    self.assertTrue(result)

  def test_parse(self):
    result = self.testobj.parse('foo bar baz')

