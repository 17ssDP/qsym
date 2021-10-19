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

class SymHandler(asyncore.dispatcher_with_send):
    
    def save_data(self, seed, lenconfig, targetList):
        f = open("path/to/save/seed", "wb")
        f.write(seed)
        f = open("path/to/save/lenconfig", "wb")
        f.write(lenconfig)

    def unpack_data(self, data):
        seedLength = stI.unpack(data[0:4])[0]
        seedData = data[4: 4 + seedLength]

        lenconfigBase = 4 + seedLength

        lenconfigLength = stI.unpack(data[lenconfigBase: lenconfigBase + 4])[0]
        lenconfigData = data[lenconfigBase + 4: lenconfigBase + 4 + lenconfigLength]

        targetBase = lenconfigBase + 4 + lenconfigLength

        targetLength = stI.unpack(data[targetBase: targetBase + 4])[0]
        targetData = data[targetBase + 4: targetBase + 4 + targetLength]

        self.save_data(seedData, lenconfigData, targetData)

    def handle_read(self):
        data = self.recv(BUFSIZ)
        # self.unpack_data(data)
        if data:
            self.send(data)

class SymServer(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.listen(5)
    
    def handle_accept(self):
        conn, addr = self.accept()
        print("Incomint connection from %s" %repr(addr))
        self.handler = SymHandler(conn)

class SymClient(asyncore.dispatcher):
    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        # self.has_data = False
        # self.data = None
        self.messages = ['1', '2', '3', '4', '5']
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((host, port))
    
    def handle_connect(self):
        pass

    def handle_read(self):
        print self.recv(1024)

    def handle_close(self):
        self.close()

    def writable(self):
        return (len(self.messages) > 0)
    
    def handle_write(self):
        # self.send(self.data)
        # self.has_data = False
        if len(self.messages) > 0:
            self.send(self.messages.pop(0))
    
    def sendData(self, data):
        self.data = data
        self.has_data = True
        self.send(self.data)

class SymServerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        server = SymServer('localhost', 8080)
        asyncore.loop()

class SymClientThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    
    def run(self):
        self.client = SymClient('localhost', 8080)
        # asyncore.loop()

    def sendData(self, data):
        self.client.sendData(data)
        

SymServerThread().start()
time.sleep(2)
SymClientThread().start()
# data = "test data"
# clientThread.sendData(data)

