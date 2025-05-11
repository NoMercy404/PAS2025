import socket

HOST = '127.0.0.1'
PORT = 12306

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print("Hostname to IP server running...")
    data, addr = s.recvfrom(1024)
    hostname = data.decode()
    try:
        ip = socket.gethostbyname(hostname)
    except Exception:
        ip = "UNKNOWN"
    s.sendto(ip.encode(), addr)