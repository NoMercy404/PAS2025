

import socket

def imap_zadanie2():
    with socket.create_connection(("212.182.24.27", 143)) as s:
        s.recv(4096)
        s.sendall(b"a1 LOGIN pasinf2017@infumcs.edu P4SInf2017\r\n")
        s.recv(4096)
        s.sendall(b"a2 SELECT INBOX\r\n")
        data = s.recv(4096).decode()

        for line in data.splitlines():
            if "EXISTS" in line:
                print("Liczba wiadomości w INBOX:", line)

        s.sendall(b"a3 LOGOUT\r\n")
        s.recv(4096)

imap_zadanie2()