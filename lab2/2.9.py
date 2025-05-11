import socket

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"  # Domyślny adres IP w przypadku błędu
    finally:
        s.close()
    return ip

def udp_client():
    server_ip = "212.182.24.27"
    server_port = 2906

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        local_ip = get_local_ip()
        print(f"Wysyłanie adresu IP: {local_ip}")

        client_socket.sendto(local_ip.encode(), (server_ip, server_port))

        data, server = client_socket.recvfrom(1024)
        hostname = data.decode()
        print(f"Otrzymana nazwa hostname: {hostname}")

    except Exception as e:
        print(f"Wystąpił błąd: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    udp_client()