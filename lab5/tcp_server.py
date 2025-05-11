import socket
import time

HOST = "127.0.0.1"
PORT = 5001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        start = time.time()
        data = conn.recv(4096)
        end = time.time()
        conn.sendall(str(end - start).encode())
