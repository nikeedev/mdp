import socket
import time

MDP_MAJOR = 1;
MDP_MINOR = 0;
MDP_PATCH = 0;
MDP_STRING = "a";

version = f"v{MDP_MAJOR}.{MDP_MINOR}.{MDP_PATCH}{MDP_STRING}"


temp_msg = f"md:// protocol - version {version} - by nikeedev\n\nHello from md:// server!\nThe server currently does not provide any content\n"

HOST = "0.0.0.0"
# According to README.md
PORT = 2004

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()
        
        with conn:
            data = conn.recv(1024)
            if not data:
                break
            print(f"{addr} requests {data.decode('utf-8')}")
            conn.send(bytes(temp_msg + f"Server time: {time.ctime()}", encoding="utf-8"))


