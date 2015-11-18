import unittest
from votemanager import votemanager

class VoteManagerTestCase(unittest.TestCase):
  def setUp(self):
    self.testobj = votemanager.VoteManager()

  def test_noVoteInProgress_atStart(self):
    self.assertFalse(self.testobj.voteInProgress)

  def test_collectVoteWhileVoteInProgress(self):
    self.testobj.collect('a')
    self.testobj.startVoting()
    self.testobj.collect('b')
    self.testobj.stopVoting()
    self.testobj.collect('c')
    self.assertEqual(self.testobj.votes, ['b'])

  def test_stoppingVoteReturnsWinner(self):
    self.testobj.startVoting()
    self.testobj.collect('a')
    self.testobj.collect('b')
    self.testobj.collect('b')
    winner = self.testobj.stopVoting()
    self.assertEqual(winner, 'b')

    
