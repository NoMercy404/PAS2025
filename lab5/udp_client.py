import socket

HOST = "127.0.0.1"
PORT = 5002

data = b"x" * 100000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(data, (HOST, PORT))
    s.settimeout(2)
    try:
        response, _ = s.recvfrom(1024)
        print("UDP czas:", response.decode())
    except socket.timeout:
        print("Brak odpowiedzi.")
