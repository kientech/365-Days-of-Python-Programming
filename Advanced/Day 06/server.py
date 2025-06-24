# Coding With Kien - 365 Days of Python Programming
# Advanced - Day 06

# Basic Chat Application (Server)
# This is the server part. Run this file first.
# Then run the client file in another terminal.

import socket

def chat_server():
    host = '127.0.0.1'
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server started, waiting for connection on {host}:{port}...")
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Client: {data.decode()}")
                
                message = input("Server: ")
                conn.sendall(message.encode())

chat_server() 