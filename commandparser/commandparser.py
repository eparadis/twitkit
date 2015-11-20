class CommandParser():
    def __init__(self, command):
        self.command = command

    def can_parse(self, text):
        return text.split()[0] == self.command

    def _parse(self, text):
        return text.split()

    def first_arg(text):
        return text.split()[1]
