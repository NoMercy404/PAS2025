import socket


def connect_to_server(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            print(f"Połączono z {host} na porcie {port}")
    except socket.error as e:
        print(f"Błąd połączenia: {e}")


host_input = input("Podaj adres IP lub nazwę hosta: ")

try:
    host = socket.gethostbyname(host_input)
    print(f"Adres IP dla {host_input}: {host}")
except socket.gaierror:
    host = host_input
    print(f"Podano bezpośrednio adres IP: {host}")

port = int(input("Podaj numer portu: "))

connect_to_server(host, port)
