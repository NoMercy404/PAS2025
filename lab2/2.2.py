import socket


def tcp_client(server_ip: str, port: int, message: str):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(5)
            sock.connect((server_ip, port))
            print("Połączono z serwerem.")

            sock.sendall(message.encode('utf-8'))  # Wysyłanie wiadomości
            print("Wiadomość wysłana:", message)

            response = sock.recv(1024)  # Odbieranie odpowiedzi
            print("Otrzymana odpowiedź:", response.decode('utf-8'))
    except socket.error as e:
        print("Błąd połączenia:", e)


if __name__ == '__main__':
    server_address = '212.182.24.27'
    server_port = 2900
    message_to_send = "Hello, server!"
    tcp_client(server_address, server_port, message_to_send)
