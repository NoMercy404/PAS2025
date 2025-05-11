import socket



target = input("Podaj adres IP lub nazwę hosta: ")

try:
    host = socket.gethostbyname(target)
    print(f"Adres IP dla {target}: {host}")
except socket.gaierror:
    host = target
    print(f"Podano bezpośrednio adres IP: {host}")

portrange = input("Wprowadz zasieg hostow (X-X): ")

start,end = portrange.split('-')
startport = int(start)
endport = int(end)

print("Skanowanie",target,"od portu",start,"do", end)
for port in range(startport,endport+1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target,port))

    if result==0:
        print('Port',port,'jest otwarty.')

        sock.close()





