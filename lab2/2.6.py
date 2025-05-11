import socket


def udp_calculator_client(server_ip: str, port: int):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.settimeout(5)

            while True:
                num1 = input("Podaj pierwszą liczbę (lub 'exit' aby zakończyć): ")
                if num1.lower() == 'exit':
                    print("Zamykanie połączenia.")
                    break

                operator = input("Podaj operator (+, -, *, /): ")
                num2 = input("Podaj drugą liczbę: ")

                message = f"{num1} {operator} {num2}"
                sock.sendto(message.encode('utf-8'), (server_ip, port))  # Wysyłanie danych

                response, _ = sock.recvfrom(4096)  # Odbieranie odpowiedzi
                print("Otrzymana odpowiedź:", response.decode('utf-8'))
    except socket.error as e:
        print("Błąd połączenia:", e)


if __name__ == '__main__':
    server_address = '127.0.0.1'
    server_port = 2902
    udp_calculator_client(server_address, server_port)
