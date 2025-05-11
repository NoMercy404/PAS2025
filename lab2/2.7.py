import socket
import sys

def get_service_name(port):
    try:
        return socket.getservbyport(port)
    except OSError:
        return "Nieznana usługa"

def connect_to_server(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5)
            s.connect((host, port))
            service_name = get_service_name(port)
            print(f"Połączono z {host} na porcie {port} ({service_name}) - Port otwarty.")
    except socket.error as e:
        print(f"Nie udało się połączyć z {host} na porcie {port} - Port zamknięty. Błąd: {e}")

if __name__ == '__main__':
    host_input = input("Podaj adres IP lub nazwę hosta: ")

    try:
        host = socket.gethostbyname(host_input)
        print(f"Adres IP dla {host_input}: {host}")
    except socket.gaierror:
        host = host_input
        print(f"Podano bezpośrednio adres IP: {host}")

    try:
        port = int(input("Podaj numer portu: "))
        connect_to_server(host, port)
    except ValueError:
        print("Nieprawidłowy numer portu.")
        sys.exit(1)
