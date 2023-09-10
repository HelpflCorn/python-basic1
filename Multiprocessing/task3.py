# Echo server with threading

# Create a socket echo server that handles each connection using the multiprocessing library.

import socket
import threading


HOST = 'localhost'
PORT = 20001

def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        client_socket.send(data)
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"Listening on {HOST}:{PORT}")

while True:
    client_sock, addr = server.accept()
    print(f"Accepted connection from {addr[0]}:{addr[1]}")
    client_thread = threading.Thread(target=handle_client, args=(client_sock,))
    client_thread.start()
