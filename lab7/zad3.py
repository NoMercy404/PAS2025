import socket

s = socket.socket()
s.connect(("212.182.24.27", 110))
s.recv(1024)

s.send(b"USER pasinf@infumcs.edu\r\n")
s.recv(1024)
s.send(b"PASS P4SInf2017\r\n")
s.recv(1024)

s.send(b"LIST\r\n")
response = s.recv(2048).decode()
print("Rozmiary wiadomości:")
print(response)

s.send(b"QUIT\r\n")
s.close()