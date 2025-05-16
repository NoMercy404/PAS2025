import socket

HOST = "127.0.0.1"
PORT = 2525  # Można użyć innego, ale nie 25 bez uprawnień root

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Serwer SMTP działa na {HOST}:{PORT}")

client_socket, addr = server_socket.accept()
print(f"Połączono z {addr}")
client_socket.send(b"220 Fake SMTP Server\r\n")

while True:
    data = client_socket.recv(1024).decode().strip()
    print(">", data)

    if data.upper().startswith("HELO") or data.upper().startswith("EHLO"):
        client_socket.send(b"250 Hello\r\n")
    elif data.upper().startswith("MAIL FROM"):
        client_socket.send(b"250 OK MAIL FROM\r\n")
    elif data.upper().startswith("RCPT TO"):
        client_socket.send(b"250 OK RCPT TO\r\n")
    elif data.upper() == "DATA":
        client_socket.send(b"354 End data with <CR><LF>.<CR><LF>\r\n")
    elif data == ".":
        client_socket.send(b"250 Message accepted for delivery\r\n")
    elif data.upper() == "QUIT":
        client_socket.send(b"221 Bye\r\n")
        break
    else:
        client_socket.send(b"502 Command not implemented\r\n")

client_socket.close()
server_socket.close()
