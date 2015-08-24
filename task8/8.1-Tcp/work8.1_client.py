__author__ = 'Administrator'
from socket import *
tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(('localhost', 21567))

while True:
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(1024)
    if not data:
        break
    print data
tcpCliSock.close()