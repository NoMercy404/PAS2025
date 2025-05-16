import socket

s = socket.socket()
s.connect(("212.182.24.27", 110))
print(s.recv(1024).decode())

s.send(b"USER pasinf@infumcs.edu\r\n")
print(s.recv(1024).decode())
s.send(b"PASS P4SInf2017\r\n")
print(s.recv(1024).decode())

s.send(b"STAT\r\n")
print(s.recv(1024).decode())

s.send(b"QUIT\r\n")
s.close()