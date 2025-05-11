import socket

HOST = '127.0.0.1'
PORT = 12305

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print("IP to Hostname server running...")
    data, addr = s.recvfrom(1024)
    ip = data.decode()
    try:
        hostname = socket.gethostbyaddr(ip)[0]
    except Exception:
        hostname = "UNKNOWN"
    s.sendto(hostname.encode(), addr)