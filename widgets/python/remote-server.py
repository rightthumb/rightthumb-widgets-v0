#!/usr/bin/python3

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QScreen
from twisted.internet import protocol, reactor

class ScreenShareProtocol(protocol.Protocol):
    def connectionMade(self):
        self.factory.clients.append(self)

    def connectionLost(self, reason):
        self.factory.clients.remove(self)

    def dataReceived(self, data):
        # Handle incoming commands here

class ScreenShareFactory(protocol.Factory):
    protocol = ScreenShareProtocol
    clients = []

    def startFactory(self):
        app = QApplication([])
        self.screen = QApplication.primaryScreen()

    def capture_screen(self):
        # Capture and return screen image
        pass

reactor.listenTCP(8000, ScreenShareFactory())
reactor.run()

# pip install twisted pyqt5
