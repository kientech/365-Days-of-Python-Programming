# Coding With Kien - 365 Days of Python Programming
# Advanced - Day 06

# Basic Chat Application (Client)
# Run the server file first, then run this file.

import socket

def chat_client():
    host = '127.0.0.1'
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print(f"Connected to server on {host}:{port}")
        while True:
            message = input("Client: ")
            s.sendall(message.encode())
            
            data = s.recv(1024)
            if not data:
                print("Connection closed by server.")
                break
            print(f"Server: {data.decode()}")

chat_client() 