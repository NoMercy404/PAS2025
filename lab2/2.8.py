import socket


def get_service_name(port):
    try:
        return socket.getservbyport(port)
    except OSError:
        return "Nieznana usługa"


target = input("Podaj adres IP lub nazwę hosta: ")

try:
    host = socket.gethostbyname(target)
    print(f"Adres IP dla {target}: {host}")
except socket.gaierror:
    host = target
    print(f"Podano bezpośrednio adres IP: {host}")

portrange = input("Wprowadz zakres portów (X-X): ")

start, end = portrange.split('-')
startport = int(start)
endport = int(end)

print("Skanowanie", target, "od portu", start, "do", end)
for port in range(startport, endport + 1):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        result = sock.connect_ex((target, port))

        if result == 0:
            service_name = get_service_name(port)
            print(f'Port {port} jest otwarty. Usługa: {service_name}')
