import unittest
from messagehandler.messagehandler import MessageHandler
from commandparser.commandparser import CommandParser
import datetime


class MessageHandlerTests(unittest.TestCase):
    def setUp(self):
        pass

    class FakeEchoCommand():
        def __init__(self, prefix):
            self.prefix = prefix
            self.message = ''

        def can_parse(self, text):
            self.message = text
            return True

        def response(self):
            return self.prefix + self.message

    class FakeNonParsing():
        def __init__(self, prefix):
            pass

        def can_parse(self, text):
            return False

    def test_no_commands_returns_none_response(self):
        mh = MessageHandler([])
        response = mh.handle_msg('test message', 'aUser', datetime.datetime(1, 1, 1))
        self.assertEqual(response, None)

    def test_one_command_returns_response(self):
        fake_echo = self.FakeEchoCommand('')
        mh = MessageHandler([fake_echo])
        response = mh.handle_msg('test message', 'someUser', datetime.datetime(1,1,1))
        self.assertEqual(response, 'test message')

    def test_first_command_passed_takes_priority(self):
        fake_a = self.FakeEchoCommand('A ')
        fake_b = self.FakeEchoCommand('B ')
        mh = MessageHandler([fake_a, fake_b])
        response = mh.handle_msg('test message', 'someUser', datetime.datetime(1,1,1))
        self.assertEqual(response, 'A test message')

    def test_priority_passes_through_commands_that_cannot_parse(self):
        never_parses = self.FakeNonParsing('nonparsing ')
        fake_echo = self.FakeEchoCommand('echo ')
        mh = MessageHandler([never_parses, fake_echo])
        response = mh.handle_msg('test message', 'someUser', datetime.datetime(1,1,1))
        self.assertEqual(response, 'echo test message')


