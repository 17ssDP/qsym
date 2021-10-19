import socket
import struct

st = struct.Struct("I")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1', 6008))

print('Bind UDP on 6008...')

while True:
    buf, addr = s.recvfrom(100 * 1024 + 8)
    
    seedSize = st.unpack(buf[0:4])[0]
    seedHead = 4
    seedTail = 4 + seedSize
    seed = buf[seedHead: seedTail]
    lenconfigHead = seedTail + 4
    lenconfigSize = buf[seedTail: seedTail + 4]
    lenconfig = buf[lenconfigHead:] 
    print("seedSize", seedSize)
    print("lenconfigSize", lenconfigSize)
    print("lenconfig", lenconfig)
    s.sendto(buf, ('127.0.0.1', 7008))