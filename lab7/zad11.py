import socket, base64, re

with socket.create_connection(("212.182.24.27", 110)) as s:
    s.recv(1024)
    s.sendall(b"USER pasinf@infumcs.edu\r\n")
    s.recv(1024)
    s.sendall(b"PASS P4SInf2017\r\n")
    s.recv(1024)
    s.sendall(b"LIST\r\n")
    lines = s.recv(4096).decode().splitlines()
    ids = [int(l.split()[0]) for l in lines[1:] if l != "."]

    for msg_id in ids:
        s.sendall(f"RETR {msg_id}\r\n".encode())
        data = s.recv(100000).decode(errors="ignore")
        if "Content-Transfer-Encoding: base64" in data:
            filename_match = re.search(r'filename="(.*?)"', data)
            if filename_match:
                filename = filename_match.group(1)
                base64_data = data.split("\r\n\r\n", 1)[1].rsplit("\r\n.", 1)[0].replace("\r\n", "")
                with open(filename, "wb") as f:
                    f.write(base64.b64decode(base64_data))
                print(f"Zapisano plik: {filename}")
                break
    s.sendall(b"QUIT\r\n")