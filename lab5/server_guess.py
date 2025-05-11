import socket
import random

HOST = "127.0.0.1"
PORT = 4000
number = random.randint(1, 100)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            try:
                guess = int(data.decode())
            except ValueError:
                conn.sendall(b"Blad: niepoprawna liczba.")
                continue

            if guess < number:
                conn.sendall(b"Za mala.")
            elif guess > number:
                conn.sendall(b"Za duza.")
            else:
                conn.sendall(b"Gratulacje, odgadles!")
                break
