import socket

HOST = '127.0.0.1'
PORT = 12304

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"UDP Calculator server on {HOST}:{PORT}")
    data, addr = s.recvfrom(1024)
    try:
        parts = data.decode().split()
        a = float(parts[0])
        op = parts[1]
        b = float(parts[2])
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            result = a / b
        else:
            result = "Invalid operator"
    except Exception as e:
        result = f"Error: {e}"
    s.sendto(str(result).encode(), addr)