import socket

def imap_zadanie5():
    with socket.create_connection(("212.182.24.27", 143)) as s:
        s.recv(4096)
        s.sendall(b"a1 LOGIN pasinf2017@infumcs.edu P4SInf2017\r\n")
        s.recv(4096)

        s.sendall(b"a2 SELECT INBOX\r\n")
        s.recv(4096)

        message_to_delete = "1"
        s.sendall(f"a3 STORE {message_to_delete} +FLAGS (\\Deleted)\r\n".encode())
        s.recv(4096)

        s.sendall(b"a4 EXPUNGE\r\n")
        print(s.recv(4096).decode())

        s.sendall(b"a5 LOGOUT\r\n")
        s.recv(4096)

imap_zadanie5()
