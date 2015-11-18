
class CommandParser():
  def __init__(self, command):
    self.command = command

  def canParse(self, text):
    return text.split()[0] is self.command

  def parse(self, text):
    return text.split() #TODO return command object or something
