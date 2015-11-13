#! /usr/bin/env python

"""A minimalistic Twitch bot.

Connects to a specific channel on twitch and dumps messages from the channel on to stdout.

Create a "twit.cfg" file in the script's directory with your connection details. The config file
looks like this:

[Twitch]
Nick: <bot's Twitch account>
Pass: <oauth credentials>
Channel: #<stream to join>

Generate an oauth token for the chatbot by logging in with your bot's account and going here:
http://www.twitchapps.com/tmi/
"""

import re
import socket
import time

CHAT_MSG=re.compile(r"^:\w+!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :")
RATE = (20.0/30)

class TwitchBot():
    """A SingleServerIRCBot that does Twitch."""

    HOST = "irc.twitch.tv"
    PORT = 6667

    def __init__(self, channel, nickname, auth):
        self._sock = socket.socket()
        self._sock.connect((self.HOST, self.PORT))
        self._sock.send("USER %s\r\n" % nickname)
        self._sock.send("PASS %s\r\n" % auth)
        self._sock.send("NICK %s\r\n" % nickname)
        self._sock.send("JOIN %s\r\n" % channel)

    def run(self):
        """Loop forever, printing messages on stdout."""
        while True:
            response = self._sock.recv(1024).decode("utf-8")
            if response == "PING :tmi.twitch.tv\r\n":
                self._sock.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
            else:
                username = re.search(r"\w+", response).group(0) # return the entire match
                message = CHAT_MSG.sub("", response)
                print(username + ": " + message)
            time.sleep(1 / RATE)

CONFIG_FILE = "twit.cfg"

def main():
    import sys
    import os.path
    import ConfigParser
    config = ConfigParser.ConfigParser()

    config.read(CONFIG_FILE)
    if not os.path.isfile(CONFIG_FILE):
        print("You must supply a twit.cfg with your Twitch details")
        sys.exit(1)

    nick = config.get("Twitch", "Nick")
    auth = config.get("Twitch", "Pass")
    channel = config.get("Twitch", "Channel")

    bot = TwitchBot(channel, nick, auth)
    bot.run()

if __name__ == "__main__":
    main()
