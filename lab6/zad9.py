import socket
import ssl
import base64

HOST = "interia.pl"
PORT = 587
USERNAME = input("Email: ")
PASSWORD = input("Hasło: ")
FROM = USERNAME
TO = input("Do kogo: ")
SUBJECT = input("Temat wiadomości: ")

HTML_BODY = """
<html>
  <body>
    <h2><b>Wiadomość HTML</b></h2>
    <p>To jest <b>pogrubiony</b>, <i>pochylony</i> i <u>podkreślony</u> tekst.</p>
  </body>
</html>
"""

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
Content-Type: text/html

{HTML_BODY}
.\r\n"""

s.send(msg.encode())
print(s.recv(1024).decode())
send("QUIT\r\n")
