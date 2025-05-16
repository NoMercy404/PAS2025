import socket

with socket.create_connection(("212.182.24.27", 110)) as s:
    s.recv(1024)
    s.sendall(b"USER pasinf@infumcs.edu\r\n")
    s.recv(1024)
    s.sendall(b"PASS P4SInf2017\r\n")
    s.recv(1024)
    s.sendall(b"LIST\r\n")
    lines = s.recv(4096).decode().splitlines()
    ids = [int(l.split()[0]) for l in lines[1:] if l != "."]
    for msg_id in ids:
        s.sendall(f"RETR {msg_id}\r\n".encode())
        print(s.recv(8192).decode())
    s.sendall(b"QUIT\r\n")