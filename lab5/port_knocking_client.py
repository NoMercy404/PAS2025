import socket
import time

SERVER_IP = "212.182.24.27"
TCP_PORT = 2913

for port in range(1024, 65536):
    if str(port).endswith("666"):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.sendto(b"PING", (SERVER_IP, port))
            s.settimeout(0.5)
            try:
                data, _ = s.recvfrom(1024)
                if data == b"PONG":
                    print(f"Port {port} OK")
                    time.sleep(0.5)
            except socket.timeout:
                continue

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((SERVER_IP, TCP_PORT))
        msg = s.recv(1024).decode()
        print("TCP Odpowiedz:", msg)
    except Exception as e:
        print("Nie udalo sie polaczyc:", e)
