import socket

HOST = "127.0.0.1"
PORT = 5001

data = b"x" * 100000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(data)
    response = s.recv(1024)
    print("TCP czas:", response.decode())
