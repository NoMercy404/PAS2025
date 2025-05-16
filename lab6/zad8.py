import socket
import ssl
import base64

boundary = "BOUNDARY-IMG"
HOST = "interia.pl"
PORT = 587
USERNAME = input("Email: ")
PASSWORD = input("Hasło: ")
FROM = USERNAME
TO = input("Do kogo: ")
SUBJECT = input("Temat: ")
BODY = input("Treść: ")
FILE = input("Zakodowany plik base64 z obrazkiem (np. encoded_image.txt): ")

with open(FILE, "r") as f:
    encoded = f.read()

s = socket.create_connection((HOST, PORT))
print(s.recv(1024).decode())

def send(cmd): s.send(cmd.encode()); print(s.recv(1024).decode())

send("EHLO test\r\n")
send("STARTTLS\r\n")
s = ssl.create_default_context().wrap_socket(s, server_hostname=HOST)
send("EHLO test\r\n")
send("AUTH LOGIN\r\n")
send(base64.b64encode(USERNAME.encode()).decode() + "\r\n")
send(base64.b64encode(PASSWORD.encode()).decode() + "\r\n")
send(f"MAIL FROM:<{FROM}>\r\n")
send(f"RCPT TO:<{TO}>\r\n")
send("DATA\r\n")

msg = f"""From: {FROM}
To: {TO}
Subject: {SUBJECT}
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary="{boundary}"

--{boundary}
Content-Type: text/plain

{BODY}

--{boundary}
Content-Type: image/jpeg; name="image.jpg"
Content-Disposition: attachment; filename="image.jpg"
Content-Transfer-Encoding: base64

{encoded}
--{boundary}--
.\r\n"""

s.send(msg.encode())
print(s.recv(1024).decode())
send("QUIT\r\n")
