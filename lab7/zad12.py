import socket

HOST = "127.0.0.1"
PORT = 1100

db_mails = [
    b"+OK 1 120\r\nFrom: test@example.com\r\nSubject: Hello\r\n\r\nHello World!\r\n.\r\n"
]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen(1)
    print("Serwer POP3 nasluchuje...")
    conn, addr = server.accept()
    with conn:
        conn.sendall(b"+OK POP3 server ready\r\n")
        while True:
            cmd = conn.recv(1024).decode().strip()
            if cmd.upper().startswith("USER"):
                conn.sendall(b"+OK user accepted\r\n")
            elif cmd.upper().startswith("PASS"):
                conn.sendall(b"+OK pass accepted\r\n")
            elif cmd.upper() == "STAT":
                conn.sendall(b"+OK 1 120\r\n")
            elif cmd.upper() == "LIST":
                conn.sendall(b"+OK\r\n1 120\r\n.\r\n")
            elif cmd.upper().startswith("RETR"):
                conn.sendall(db_mails[0])
            elif cmd.upper() == "QUIT":
                conn.sendall(b"+OK Bye\r\n")
                break
            else:
                conn.sendall(b"-ERR Command not recognized\r\n")