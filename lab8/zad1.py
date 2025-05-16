import socket
import ssl

def imap_zadanie1():
    HOST = "212.182.24.27"
    PORT = 143

    s = socket.create_connection((HOST, PORT))
    recv = s.recv(4096)
    print("1:", recv.decode())

    # Logowanie
    s.sendall(b"a1 LOGIN pasinf2017@infumcs.edu P4SInf2017\r\n")
    print("2:", s.recv(4096).decode())

    # Wybór skrzynki
    s.sendall(b"a2 SELECT INBOX\r\n")
    print("3:", s.recv(4096).decode())

    # Pobranie 1. wiadomości
    s.sendall(b"a3 FETCH 1 BODY[TEXT]\r\n")
    print("4:", s.recv(8192).decode())

    # Oznaczenie jako przeczytana
    s.sendall(b"a4 STORE 1 +FLAGS (\\Seen)\r\n")
    print("5:", s.recv(4096).decode())

    # Zamknięcie połączenia
    s.sendall(b"a5 LOGOUT\r\n")
    print("6:", s.recv(4096).decode())

    s.close()

imap_zadanie1()
