import socket

s = socket.socket()
s.connect(("212.182.24.27", 110))
s.recv(1024)
s.send(b"USER pasinf@infumcs.edu\r\n")
s.recv(1024)
s.send(b"PASS P4SInf2017\r\n")
s.recv(1024)
s.send(b"LIST\r\n")
lines = s.recv(2048).decode().splitlines()

msgs = [(int(line.split()[0]), int(line.split()[1])) for line in lines[1:] if line != "."]
max_msg = max(msgs, key=lambda x: x[1])[0]

s.send(f"RETR {max_msg}\r\n".encode())
data = s.recv(4096).decode()
print("Treść największej wiadomości:")
print(data)

s.send(b"QUIT\r\n")
s.close()