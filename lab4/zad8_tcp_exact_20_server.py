import socket

HOST = '127.0.0.1'
PORT = 12308

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print("Serwer czeka na 20 znaków...")
    conn, addr = s.accept()
    with conn:
        data = b''
        while len(data) < 20:
            packet = conn.recv(20 - len(data))
            if not packet:
                break
            data += packet
        conn.sendall(data)