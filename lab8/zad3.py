import socket

def imap_zadanie3():
    with socket.create_connection(("212.182.24.27", 143)) as s:
        s.recv(4096)
        s.sendall(b"a1 LOGIN pasinf2017@infumcs.edu P4SInf2017\r\n")
        s.recv(4096)
        s.sendall(b"a2 LIST \"\" *\r\n")
        foldery = s.recv(8192).decode()
        print("Dostępne skrzynki:")
        print(foldery)

        for line in foldery.splitlines():
            if '"/"' in line:
                box = line.split('"')[-2]
                tag = f"x{hash(box)%10000}".encode()
                cmd = tag + b" SELECT \"" + box.encode() + b"\"\r\n"
                s.sendall(cmd)
                resp = s.recv(4096).decode()
                for l in resp.splitlines():
                    if "EXISTS" in l:
                        print(f"Skrzynka {box}: {l}")

        s.sendall(b"a9 LOGOUT\r\n")
        s.recv(4096)

imap_zadanie3()