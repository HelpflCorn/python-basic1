# Echo server with threading

# Create a socket echo server which handles each connection in a separate Thread


import socket
import threading

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024
msgFromServer = "UDP, UDP"
bytesToSend = str.encode(msgFromServer)

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

def handle_client(bytesAddressPair):
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)
    
    UDPServerSocket.sendto(bytesToSend, address)

while True:
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    client_handler = threading.Thread(target=handle_client, args=(bytesAddressPair,))
    client_handler.start()
