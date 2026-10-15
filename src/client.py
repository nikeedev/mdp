import socket
import sys

MDP_MAJOR = 1;
MDP_MINOR = 0;
MDP_PATCH = 0;
MDP_STRING = "a";

version = f"v{MDP_MAJOR}.{MDP_MINOR}.{MDP_PATCH}{MDP_STRING}"

if len(sys.argv) < 2:
    print("No URL provided")
    print(f"mdp:// client - version {version} - by nikeedev")
    print(f"Usage: {sys.argv[0]} <mdp:// URL> ")
    exit(1)

protocol = "mdp://"
url = sys.argv[1]

if not url.startswith(protocol):
    url = protocol + url

if len(url) > 1024:
    print(f"The URL too long (length: {len(url)}), must be less or equal to 1024 characters.")
    exit(1)


without_md = url.split(protocol)[1]

serverAddr = without_md.split("/")[0]

port = 2004
msg = url
print(f"Connecting to {serverAddr}:{port}")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((serverAddr, port))
s.send(bytes(msg, encoding="utf-8"))

output = ""
while True:
    data = s.recv(1024)
    if data == b'':
        break
    
    output += data.decode("utf-8")
    # print(output)
s.close()

print(output)

