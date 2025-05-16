import socket

s = socket.socket()
s.connect(("212.182.24.27", 110))
print(s.recv(1024).decode())

s.send(b"USER pasinf@infumcs.edu\r\n")
s.recv(1024)
s.send(b"PASS P4SInf2017\r\n")
s.recv(1024)

s.send(b"STAT\r\n")
print("Suma bajtow:", s.recv(1024).decode().split()[2])

s.send(b"QUIT\r\n")
s.close()