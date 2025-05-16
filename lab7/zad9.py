import socket

with socket.create_connection(("212.182.24.27", 110)) as s:
    s.recv(1024)
    s.sendall(b"USER pasinf@infumcs.edu\r\n")
    s.recv(1024)
    s.sendall(b"PASS P4SInf2017\r\n")
    s.recv(1024)
    s.sendall(b"LIST\r\n")
    lines = s.recv(4096).decode().splitlines()
    msgs = [(int(l.split()[0]), int(l.split()[1])) for l in lines[1:] if l != "."]
    max_id = max(msgs, key=lambda x: x[1])[0]
    s.sendall(f"RETR {max_id}\r\n".encode())
    print(s.recv(8192).decode())
    s.sendall(b"QUIT\r\n")