import socket

with socket.create_connection(("212.182.24.27", 110)) as s:
    s.recv(1024)
    s.sendall(b"USER pasinf@infumcs.edu\r\n")
    s.recv(1024)
    s.sendall(b"PASS P4SInf2017\r\n")
    s.recv(1024)
    s.sendall(b"LIST\r\n")
    response = s.recv(4096).decode()
    print("Rozmiary wiadomości:")
    print(response)
    s.sendall(b"QUIT\r\n")