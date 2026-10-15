import socket
import time
import sys

MDP_MAJOR = 1;
MDP_MINOR = 0;
MDP_PATCH = 0;
MDP_STRING = "a";

version = f"v{MDP_MAJOR}.{MDP_MINOR}.{MDP_PATCH}{MDP_STRING}"

if len(sys.argv) < 2:
    print(f"mdp:// server - version {version} - by nikeedev")
    print(f"Too few arguments passed")
    print(f"Usage: {sys.argv[0]} <root folder/serving folder>")
    print("\troot folder: the server will pass all the files that are within that folder under the root path of the server (aka. example.com/file.md")
    exit(1)

root = sys.argv[1]

temp_msg = f"Hello from mdp:// server!\nThe server currently does not provide any content\n\nmdp:// server - version {version} - by nikeedev"

HOST = "0.0.0.0"
# According to README.md
PORT = 2004

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Serving mdp:// on {PORT}, on root {root}")

    while True:
        conn, addr = server_socket.accept()
        
        with conn:
            data = conn.recv(1024)
            if not data:
                break
            print(f"{addr} requests {data.decode('utf-8')}")
            conn.send(bytes(temp_msg + f"\nServer clock (not localtime): {time.ctime()}\r\n", encoding="utf-8"))


