
class CommandParser():
  def __init__(self, command):
    self.command = command

  def canParse(self, text):
    return text.split()[0] == self.command

  def _parse(self, text):
    return text.split()

  def firstArg(self, text):
    return text.split()[1]
