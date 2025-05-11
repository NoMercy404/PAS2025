import socket

HOST = '127.0.0.1'
PORT = 12303

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Serwer UDP nasłuchuje na {HOST}:{PORT}")
    data, addr = s.recvfrom(1024)
    print("Odebrano:", data.decode(), "od", addr)
    s.sendto(data, addr)