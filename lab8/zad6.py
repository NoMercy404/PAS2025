import socket

def imap_serwer():
    host = "127.0.0.1"
    port = 8143

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        print(f"Serwer IMAP nasłuchuje na {host}:{port}...")
        conn, addr = s.accept()
        with conn:
            print(f"Połączono z {addr}")
            conn.sendall(b"* OK IMAP4rev1 Service Ready\r\n")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                command = data.decode().strip()
                print(f"Odebrano: {command}")
                if "LOGIN" in command:
                    conn.sendall(b"a1 OK LOGIN completed\r\n")
                elif "SELECT" in command:
                    conn.sendall(b"* 3 EXISTS\r\n* 0 RECENT\r\na2 OK [READ-WRITE] SELECT completed\r\n")
                elif "FETCH" in command:
                    conn.sendall(b"* 1 FETCH (BODY[TEXT] {30}\r\nTo jest testowa wiadomosc.\r\n)\r\na3 OK FETCH completed\r\n")
                elif "LOGOUT" in command:
                    conn.sendall(b"* BYE IMAP4rev1 Server logging out\r\na4 OK LOGOUT completed\r\n")
                    break
                else:
                    conn.sendall(b"a0 BAD Command not implemented\r\n")

imap_serwer()
