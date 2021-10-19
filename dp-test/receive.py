from socket import *
from time import ctime
import struct

stI = struct.Struct("I")

HOST = ''
PORT = 6008
BUFSIZ = 1024 * 100
ADDRESS = (HOST, PORT)

udpServerSocket = socket(AF_INET, SOCK_DGRAM)
udpServerSocket.bind(ADDRESS)

while True:
    print("waiting for message...")
    data, addr = udpServerSocket.recvfrom(BUFSIZ)

    seedLength = stI.unpack(data[0:4])[0]
    seedData = data[4: 4 + seedLength]

    lenconfigBase = seedLength + 4

    lenconfigLength = stI.unpack(data[lenconfigBase: lenconfigBase + 4])[0]
    lenconfigData = data[lenconfigBase + 4: lenconfigBase + 4 + lenconfigLength]

    f = open("path/to/save/seed", "wb")
    f.write(seedData)
    f = open("path/to/save/lenconfig", "wb")
    f.write(lenconfigData)

    content = '[%s] %s' % (bytes(ctime()), data)
    udpServerSocket.sendto(content, addr)
    print('...received from and returned to:', addr)

udpServerSocket.close()