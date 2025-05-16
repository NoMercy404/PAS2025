import socket
import ssl
import base64

def send_and_print(s, msg):
    s.send(msg.encode())
    print(s.recv(1024).decode())

HOST = "interia.pl"
PORT = 587
USERNAME = input("Podaj login e-mail: ")
PASSWORD = input("Podaj hasło: ")
FROM = USERNAME
TO = input("Podaj adres odbiorcy: ")
SUBJECT = input("Podaj temat wiadomości: ")
BODY = input("Podaj treść wiadomości: ")

s = socket.create_connection((HOST, PORT))
print(s.recv(1024).decode())

send_and_print(s, "EHLO local.test\r\n")
send_and_print(s, "STARTTLS\r\n")

s = ssl.create_default_context().wrap_socket(s, server_hostname=HOST)
send_and_print(s, "EHLO local.test\r\n")
send_and_print(s, "AUTH LOGIN\r\n")
send_and_print(s, base64.b64encode(USERNAME.encode()).decode() + "\r\n")
send_and_print(s, base64.b64encode(PASSWORD.encode()).decode() + "\r\n")
send_and_print(s, f"MAIL FROM:<{FROM}>\r\n")
send_and_print(s, f"RCPT TO:<{TO}>\r\n")
send_and_print(s, "DATA\r\n")

msg = f"From: {FROM}\nTo: {TO}\nSubject: {SUBJECT}\n\n{BODY}\n.\r\n"
s.send(msg.encode())
print(s.recv(1024).decode())
send_and_print(s, "QUIT\r\n")
