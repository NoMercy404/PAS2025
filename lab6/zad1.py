import socket
import ssl
import base64

HOST = "interia.pl"
PORT = 587
USERNAME = "pas2017@interia.pl"
PASSWORD = "P4SInf2017"
FROM = USERNAME
TO = "example@example.com"

# Połączenie z serwerem
client_socket = socket.create_connection((HOST, PORT))
recv = client_socket.recv(1024).decode()
print(recv)

client_socket.send(b"EHLO test.local\r\n")
recv = client_socket.recv(1024).decode()
print(recv)

# STARTTLS
client_socket.send(b"STARTTLS\r\n")
recv = client_socket.recv(1024).decode()
print(recv)

# TLS
context = ssl.create_default_context()
client_socket = context.wrap_socket(client_socket, server_hostname=HOST)

client_socket.send(b"EHLO test.local\r\n")
recv = client_socket.recv(1024).decode()
print(recv)

# AUTH LOGIN
client_socket.send(b"AUTH LOGIN\r\n")
recv = client_socket.recv(1024).decode()
print(recv)

client_socket.send(base64.b64encode(USERNAME.encode()) + b"\r\n")
recv = client_socket.recv(1024).decode()
print(recv)

client_socket.send(base64.b64encode(PASSWORD.encode()) + b"\r\n")
recv = client_socket.recv(1024).decode()
print(recv)

# Dane emaila
client_socket.send(f"MAIL FROM:<{FROM}>\r\n".encode())
recv = client_socket.recv(1024).decode()
print(recv)

client_socket.send(f"RCPT TO:<{TO}>\r\n".encode())
recv = client_socket.recv(1024).decode()
print(recv)

client_socket.send(b"DATA\r\n")
recv = client_socket.recv(1024).decode()
print(recv)

message = f"""From: {FROM}
To: {TO}
Subject: Test from Python ESMTP

This is a test message sent using ESMTP via telnet simulation.
.
"""
client_socket.send(message.encode())
client_socket.send(b"\r\n.\r\n")
recv = client_socket.recv(1024).decode()
print(recv)

client_socket.send(b"QUIT\r\n")
recv = client_socket.recv(1024).decode()
print(recv)

client_socket.close()
