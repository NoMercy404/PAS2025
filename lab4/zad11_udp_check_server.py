import socket

HOST = '127.0.0.1'
PORT = 12311

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print("Serwer walidacji działa...")
    data, addr = s.recvfrom(1024)
    msg = data.decode()
    if msg.startswith("check:"):
        response = "TAK" if len(msg) > 6 else "NIE"
    else:
        response = "BAD SYNTAX"
    s.sendto(response.encode(), addr)