import unittest

from votemanager import votemanager
from commandparser import commandparser

class IntegrationTests(unittest.TestCase):

  def test_voting(self):
    vm = votemanager.VoteManager()
    parser = commandparser.CommandParser('vote')
    incomingMsgs = [ 'vote a', 'vote b', 'foobar', 'vote a']
    
    vm.startVoting()
    for msg in incomingMsgs:
      if parser.canParse(msg):
        vm.collect( parser.firstArg(msg))
    winner = vm.stopVoting()

    self.assertEqual(winner, 'a')
