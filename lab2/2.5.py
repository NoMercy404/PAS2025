import socket


def udp_client(server_ip: str, port: int):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.settimeout(5)

            while True:
                message = input("Wpisz wiadomość (lub 'exit' aby zakończyć): ")
                if message.lower() == 'exit':
                    print("Zamykanie połączenia.")
                    break

                sock.sendto(message.encode('utf-8'), (server_ip, port))  # Wysyłanie wiadomości
                response, _ = sock.recvfrom(1024)  # Odbieranie odpowiedzi
                print("Otrzymana odpowiedź:", response.decode('utf-8'))
    except socket.error as e:
        print("Błąd połączenia:", e)


if __name__ == '__main__':
    server_address = '212.182.24.27'
    server_port = 2901
    udp_client(server_address, server_port)