__author__ = 'Administrator'
import socket
host='127.0.0.1'
port=23457
bufsiz=1024
ADDR=(host,port)
udpCliSock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    clientData=raw_input('>')
    if not clientData:
        break
    udpCliSock.sendto(clientData,ADDR)
    data,ADDR=udpCliSock.recvfrom(bufsiz)
    print data
udpCliSock.close()