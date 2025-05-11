import socket

SERVER_IP = "212.182.24.27"
SERVER_PORT = 2912

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_IP, SERVER_PORT))
    while True:
        guess = input("Podaj liczbę: ")
        s.sendall(guess.encode())
        response = s.recv(1024).decode()
        print("Serwer:", response)
        if "odgadłeś" in response.lower():
            break
