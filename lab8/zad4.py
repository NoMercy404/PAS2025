import socket

def imap_zadanie4():
    with socket.create_connection(("212.182.24.27", 143)) as s:
        s.recv(4096)
        s.sendall(b"a1 LOGIN pasinf2017@infumcs.edu P4SInf2017\r\n")
        s.recv(4096)
        s.sendall(b"a2 SELECT INBOX\r\n")
        s.recv(4096)

        # Szukanie nieprzeczytanych wiadomości
        s.sendall(b"a3 SEARCH UNSEEN\r\n")
        data = s.recv(4096).decode()
        print("Nieprzeczytane ID:", data)

        ids = []
        for line in data.splitlines():
            if line.startswith("* SEARCH"):
                ids = line.strip().split()[2:]  # omijamy "* SEARCH"

        for msg_id in ids:
            print(f"\n--- Wiadomość {msg_id} ---")
            s.sendall(f"a4 FETCH {msg_id} BODY[TEXT]\r\n".encode())
            print(s.recv(8192).decode())

            s.sendall(f"a5 STORE {msg_id} +FLAGS (\\Seen)\r\n".encode())
            s.recv(4096)

        s.sendall(b"a6 LOGOUT\r\n")
        s.recv(4096)

imap_zadanie4()
