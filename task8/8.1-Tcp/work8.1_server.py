__author__ = 'Administrator'
import socket
from time import ctime
tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSerSock.bind(('localhost', 21567))
tcpSerSock.listen(5)
while True:
    print 'waiting for connection.....'
    tcpCliSock, addr = tcpSerSock.accept()
    print '...conneced from:', addr
    while True:
       data = tcpCliSock.recv(1024)
       if not data:
           break
       tcpCliSock.send('[%s] %s' % (ctime(), data))
    tcpCliSock.close()
tcpSerSock.close()