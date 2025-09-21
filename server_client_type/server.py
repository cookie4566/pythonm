# basic server boiler plate
#echos a message back to client 
import socket

HOST = "127.0.0.1" # Constant that sets the host IP to local machine
PORT = 65432 # Port that is listened too

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)