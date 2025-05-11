import socket

HOST = '127.0.0.1'
PORT = 12307

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print("Serwer czeka na wiadomość (max 20 znaków)...")
    conn, addr = s.accept()
    with conn:
        data = conn.recv(20)
        conn.sendall(data)