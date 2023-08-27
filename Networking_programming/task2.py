# Task 2

# Extend the echo server, which returns to client the data, 
# encrypted using the Caesar cipher algorithm by a specific key obtained from the client.

import socket

def caesar_cipher(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - shift + key) % 26 + shift)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

HOST = '127.0.0.1'
PORT = 65432

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((HOST, PORT))

    while True:
        data, addr = sock.recvfrom(1024)
        if not data:
            break

        key, message = map(int, data.decode().split(','))
        
        encrypted_message = caesar_cipher(message, key)

        print(f"Received: Key={key}, Message={message}, Encrypted={encrypted_message}")
        sock.sendto(encrypted_message.encode(), addr)

if __name__ == "__main__":
    main()

print(caesar_cipher("I am very tired and it doesn't get any better", 3))