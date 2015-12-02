class MessageHandler():
    def __init__(self, commands):
        self.commands = commands

    def handle_msg(self, message, username, datetime):
        for command in self.commands:
            if command.can_parse(message):
                return command.response()
        return None
