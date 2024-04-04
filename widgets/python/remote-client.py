#!/usr/bin/python3

from twisted.internet import reactor, protocol

class RemoteControlProtocol(protocol.Protocol):
    def connectionMade(self):
        self.sendCommand('connect')

    def sendCommand(self, command):
        self.transport.write(command.encode())

    def dataReceived(self, data):
        # Process incoming screen data

class RemoteControlFactory(protocol.ClientFactory):
    protocol = RemoteControlProtocol

reactor.connectTCP("server_address_here", 8000, RemoteControlFactory())
reactor.run()

# pip install twisted pyqt5
