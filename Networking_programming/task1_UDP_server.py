# During the lesson, we have created a server and client, which use TCP/IP
# protocol for communication via sockets. In this task, 
# you have to create a server and client, which will use 
# user datagram protocol (UDP) for communication.

import socket

localIP = "127.0.0.1"

localPort = 20001

bufferSize = 1024

msgFromServer = "UDP, UDP"

bytesToSend = str.encode(msgFromServer)

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket.bind((localIP, localPort))

 

print("UDP server up and listening")


while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)

   

    UDPServerSocket.sendto(bytesToSend, address)