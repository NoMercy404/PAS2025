import socket
import ssl
import base64

HOST = "interia.pl"
PORT = 587
USERNAME = "pas2017@interia.pl"
PASSWORD = "P4SInf2017"
FROM = USERNAME
TO = ["example1@example.com", "example2@example.com"]

# Połączenie z serwerem
client_socket = socket.create_connection((HOST, PORT))
print(client_socket.recv(1024).decode())

client_socket.send(b"EHLO test.local\r\n")
print(client_socket.recv(1024).decode())

# STARTTLS
client_socket.send(b"STARTTLS\r\n")
print(client_socket.recv(1024).decode())

# TLS
context = ssl.create_default_context()
client_socket = context.wrap_socket(client_socket, server_hostname=HOST)

client_socket.send(b"EHLO test.local\r\n")
print(client_socket.recv(1024).decode())

# AUTH LOGIN
client_socket.send(b"AUTH LOGIN\r\n")
print(client_socket.recv(1024).decode())

client_socket.send(base64.b64encode(USERNAME.encode()) + b"\r\n")
print(client_socket.recv(1024).decode())

client_socket.send(base64.b64encode(PASSWORD.encode()) + b"\r\n")
print(client_socket.recv(1024).decode())

# Dane emaila
client_socket.send(f"MAIL FROM:<{FROM}>\r\n".encode())
print(client_socket.recv(1024).decode())

# Kilku odbiorców
for recipient in TO:
    client_socket.send(f"RCPT TO:<{recipient}>\r\n".encode())
    print(client_socket.recv(1024).decode())

client_socket.send(b"DATA\r\n")
print(client_socket.recv(1024).decode())

message = f"""From: {FROM}
To: {", ".join(TO)}
Subject: Email to multiple recipients

This is a test message sent to multiple recipients using ESMTP.
.
"""
client_socket.send(message.encode())
client_socket.send(b"\r\n.\r\n")
print(client_socket.recv(1024).decode())

client_socket.send(b"QUIT\r\n")
print(client_socket.recv(1024).decode())

client_socket.close()
