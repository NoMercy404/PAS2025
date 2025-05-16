import socket

with socket.create_connection(("212.182.24.27", 110)) as s:
    s.recv(1024)
    s.sendall(b"USER pasinf@infumcs.edu\r\n")
    s.recv(1024)
    s.sendall(b"PASS P4SInf2017\r\n")
    s.recv(1024)
    s.sendall(b"STAT\r\n")
    stat = s.recv(1024).decode()
    print("Liczba wiadomości:", stat.split()[1])
    s.sendall(b"QUIT\r\n")