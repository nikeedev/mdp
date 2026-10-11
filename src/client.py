import socket
import sys

if len(sys.argv) < 2:
    print("No URL provided")
    print("")
    print(f"Usage: {sys.argv[0]}")
    exit(1)

url = sys.argv[1]

port = 2004


BUFFER_SIZE = 1024

msg = url

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()
