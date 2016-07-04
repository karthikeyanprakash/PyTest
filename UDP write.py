import numpy as np
import socket
x = np.array_str(np.arange(10))
print x

UDP_IP = "192.168.100.28"
UDP_PORT = 61557
MESSAGE = x
print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))