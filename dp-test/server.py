import socket
import time
import struct
import asyncore
import threading
import os

stI = struct.Struct("I")

HOST = ''
PORT = 6008
BUFSIZ = 1024 * 100
ADDRESS = (HOST, PORT)
class SymHandler(asyncore.dispatcher):
   
    def __init__(self, socket, output, fuzzer):
        asyncore.dispatcher.__init__(self, socket)
        self.output = output
        self.fuzzer = fuzzer
        self.index = 0

class SymServer(asyncore.dispatcher):

    def __init__(self, host, port, output, fuzzer):
        asyncore.dispatcher.__init__(self)
        self.output = output
        self.fuzzer = fuzzer
        self.create_socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.set_reuse_addr()
        self.bind((host, port))
        self.index = 0
        # self.listen(5)
    
    @property
    def fuzzer_dir(self):
        return os.path.join(self.output, self.fuzzer)

    @property
    def fuzzer_queue(self):
        return os.path.join(self.fuzzer_dir, "queue")

    @property
    def fuzzer_lenconfig(self):
        return os.path.join(self.fuzzer_queue, ".state/lenconfig")
    
    @property
    def fuzzer_target(self):
        return os.path.join(self.fuzzer_queue, ".state/target")

    def save_data(self, seed, lenconfig, targetList):
        filename = os.path.join(self.fuzzer_queue,
                        "id:%06d" % (self.index))
        f = open(filename, "wb")
        f.write(seed)
        configname = os.path.join(self.fuzzer_lenconfig,
                        "id:%06d,lenconfig" % (self.index))
        f = open(configname, "wb")
        f.write(lenconfig)
        targetname = os.path.join(self.fuzzer_target,
                        "id:%06d,target" % (self.index))
        f = open(targetname, "wb")
        f.write(targetList)
        self.index += 1

    def unpack_data(self, data):
        print self.fuzzer
        seedLength = stI.unpack(data[0:4])[0]
        seedData = data[4: 4 + seedLength]

        lenconfigBase = 4 + seedLength

        lenconfigLength = stI.unpack(data[lenconfigBase: lenconfigBase + 4])[0]
        lenconfigData = data[lenconfigBase + 4: lenconfigBase + 4 + lenconfigLength]

        targetBase = lenconfigBase + 4 + lenconfigLength

        targetLength = stI.unpack(data[targetBase: targetBase + 4])[0]
        targetData = data[targetBase + 4: targetBase + 4 + targetLength]

        # targetData = "target"

        self.save_data(seedData, lenconfigData, targetData)

        # self.handler = SymHandler(conn, self.output, self.fuzzer)

    def handle_accept(self):
        conn, addr = self.accept()
        print("Incomint connection from %s" %repr(addr))
        self.handler = SymHandler(conn, self.output, self.fuzzer)
    
    def handle_read(self):
        data, addr = self.recvfrom(1024 * 100 + 8)
        print("Incomint UDP connection from %s" %repr(addr))
        self.unpack_data(data)

class SymServerThread(threading.Thread):
    
    def __init__(self, output, fuzzer):
        threading.Thread.__init__(self)
        self.output = output
        self.fuzzer = fuzzer

    def run(self):
        server = SymServer('localhost', PORT, self.output, self.fuzzer)
        asyncore.loop()

server = SymServerThread("/home/dp/qsym-area/qsym/dp-test/psy", "fuzzer")

server.start()