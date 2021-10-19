import socket
import time
import struct
import asyncore
import threading

stI = struct.Struct("I")

HOST = ''
PORT = 6008
BUFSIZ = 1024 * 100
ADDRESS = (HOST, PORT)

class SymClient(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
        self.has_data = False
        self.data = None
    
    @property
    def messages(self):
        f = open("/home/dp/dp-test/qsym_test/resultPointer/corpus/initcorpus", "rb")
        seedData = f.read()
        data = stI.pack(len(seedData))#"\x08\x00\x00\x00"
        print data
        data += seedData
        print data
        f = open("/home/dp/dp-test/qsym_test/resultPointer/lenconfig", "rb")
        lengconfigData = f.read()
        data += stI.pack(len(lengconfigData))#"\x08\x00\x00\x00"
        print data
        data += lengconfigData
        print data
        return data

    def handle_connect(self):
        pass

    def handle_close(self):
        self.close()

    def handle_read(self):
        print self.recv(1024)

    def writable(self):
        return self.has_data
    
    def handle_write(self):
        # self.send(self.data)
        # self.has_data = False
        if len(self.data) > 0:
            print self.data
            length = self.send(self.messages)
            print("length = %d", length)
        self.has_data = False
    
    def sendData(self, data):
        self.data = data

class SymClientThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.client = SymClient('localhost', 6008)
    
    def run(self):
        asyncore.loop()

    def sendData(self, data):
        self.client.sendData(data)

client = SymClientThread()
client.start()
client.sendData("data1")
client.sendData("data2")
