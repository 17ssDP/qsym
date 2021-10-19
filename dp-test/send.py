from socket import *
import struct

stI = struct.Struct("I")

HOST = '127.0.0.1'
PORT = 7008
BUFSIZ = 1024
ADDRESS = (HOST, PORT)

class SymClient():

    def __init__(self):
        self.socket = socket(AF_INET, SOCK_DGRAM)

    def sendData(self, seed, lenconfig):
        f = open(seed, "rb")
        seedData = f.read()
        data = stI.pack(len(seedData))#"\x08\x00\x00\x00"
        data += seedData
        f = open(lenconfig, "rb")
        lengconfigData = f.read()
        data += stI.pack(len(lengconfigData))#"\x08\x00\x00\x00"
        data += lengconfigData
        self.socket.sendto(data, ADDRESS)

    def close(self):
        self.socket.close()
client = SymClient()
client.sendData("seed", "lengconfig")
client.close()
