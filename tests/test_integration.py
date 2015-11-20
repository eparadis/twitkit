import unittest
from votemanager import votemanager
from commandparser import commandparser


class IntegrationTests(unittest.TestCase):
    def test_voting(self):
        vm = votemanager.VoteManager()
        parser = commandparser.CommandParser('vote')
        incomingmsgs = ['vote a', 'vote b', 'foobar', 'vote a']

        vm.startVoting()
        for msg in incomingmsgs:
            if parser.can_parse(msg):
                vm.collect(commandparser.CommandParser.first_arg(msg))
        winner = vm.stopVoting()

        self.assertEqual(winner, 'a')
