from collections import Counter

class VoteManager():
  def __init__(self):
    self.voteInProgress = False
    self.votes = []

  def collect(self, vote):
    if self.voteInProgress:
      self.votes.append(vote)

  def startVoting(self):
    self.votes = []
    self.voteInProgress = True

  def stopVoting(self):
    self.voteInProgress = False
    winner = Counter(self.votes).most_common(1)
    if winner is not None:
      return winner[0][0]
    else:
      return None
