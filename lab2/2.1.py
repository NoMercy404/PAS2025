import socket
def get_ntp_time(server: str, port: int =13 ) -> str:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(5)
            sock.connect((server, port))
            print("Połączono z serwerem NTP.")
            data = sock.recv(1024)  # Odbieranie danych
            return data.decode('utf-8').strip()
    except socket.error as e:
        return f"Błąd połączenia: {e}"

if __name__ == '__main__':
    server_address = 'google.pl'
    ntp_time = get_ntp_time(server_address)
    print("Odebrana data i czas:", ntp_time)
