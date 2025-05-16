import socket
import ssl
import base64

HOST = "interia.pl"
PORT = 587
USERNAME = "pas2017@interia.pl"
PASSWORD = "P4SInf2017"
FROM = USERNAME
TO = "example@example.com"

# Wczytaj zawartość pliku zakodowanego base64
with open("file_encoded.txt", "r") as f:
    encoded_file = f.read()

boundary = "BOUNDARY123"

# Połączenie
client_socket = socket.create_connection((HOST, PORT))
print(client_socket.recv(1024).decode())

client_socket.send(b"EHLO test.local\r\n")
print(client_socket.recv(1024).decode())

client_socket.send(b"STARTTLS\r\n")
print(client_socket.recv(1024).decode())

context = ssl.create_default_context()
client_socket = context.wrap_socket(client_socket, server_hostname=HOST)

client_socket.send(b"EHLO test.local\r\n")
print(client_socket.recv(1024).decode())

client_socket.send(b"AUTH LOGIN\r\n")
print(client_socket.recv(1024).decode())

client_socket.send(base64.b64encode(USERNAME.encode()) + b"\r\n")
print(client_socket.recv(1024).decode())

client_socket.send(base64.b64encode(PASSWORD.encode()) + b"\r\n")
print(client_socket.recv(1024).decode())

client_socket.send(f"MAIL FROM:<{FROM}>\r\n".encode())
print(client_socket.recv(1024).decode())

client_socket.send(f"RCPT TO:<{TO}>\r\n".encode())
print(client_socket.recv(1024).decode())

client_socket.send(b"DATA\r\n")
print(client_socket.recv(1024).decode())

# MIME email z załącznikiem
message = f"""From: {FROM}
To: {TO}
Subject: Email with text attachment
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="{boundary}"

--{boundary}
Content-Type: text/plain

This email contains a text file as attachment.

--{boundary}
Content-Type: text/plain; name="file.txt"
Content-Disposition: attachment; filename="file.txt"
Content-Transfer-Encoding: base64

{encoded_file}
--{boundary}--
.
"""

client_socket.send(message.encode())
client_socket.send(b"\r\n.\r\n")
print(client_socket.recv(1024).decode())

client_socket.send(b"QUIT\r\n")
print(client_socket.recv(1024).decode())

client_socket.close()
