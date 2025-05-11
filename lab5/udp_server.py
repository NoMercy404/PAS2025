import socket
import time

HOST = "127.0.0.1"
PORT = 5002

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    data, addr = s.recvfrom(4096)
    start = time.time()
    end = time.time()
    s.sendto(str(end - start).encode(), addr)
