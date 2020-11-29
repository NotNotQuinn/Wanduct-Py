from util.infinateTimer import InfiniteTimer
from util.parser import parsemsg
import socket


class WanductBot():
    def __init__(self, options: dict):
        self.socket = socket.socket()
        self.options = options
    def _send_raw(self, txt):
        


(prefix, command, args) = parsemsg("test")
print (f"\nPrefix: " + prefix + "\nCommand: " + command + "\nArgs:", args)
