import socket

HOST = '127.0.0.1'
PORT = 12302

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"Serwer nasłuchuje na {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print('Połączono z', addr)
        data = conn.recv(1024)
        print("Odebrano:", data.decode())
        conn.sendall(data)