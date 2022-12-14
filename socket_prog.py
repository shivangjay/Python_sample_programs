import socket

HOST = "0.0.0.0"  # Standard loopback interface address (localhost)
PORT = 5000  # Port to listen on (non-privileged ports are > 1023)
file="data.csv"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            print(data)
            f=open(file,'a')
            f.write(data.decode("utf-8")+"\n")
            f.close()
            if not data:
                break
            conn.sendall(data)