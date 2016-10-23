from NetChannel import NetChannel
from time import sleep
import socket

UPDATE_TIME_SEC = 3

class TxChannel(NetChannel):
    def __init__(self, name, messageSender, socket):
        self.socket = socket
        NetChannel.__init__(self, name="TX-"+name)
        self.messageSender = messageSender

    def run(self):
        self.messageSender.send(self.socket, "HELLO")

        
        self.socket.recv()

        alive = True
        while alive:
            sleep(UPDATE_TIME_SEC)
            alive = self.messageSender.send(self.socket, "KeepAlive")
