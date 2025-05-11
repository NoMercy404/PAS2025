import socket

ip = str(input("Wprowadz IP: "))

print(socket.gethostbyaddr(ip))