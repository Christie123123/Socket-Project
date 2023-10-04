import sys,os,socket


if len(sys.argv) != 3:
    print("Usage: python client.py <server> <output file>")
    exit(1)

hostname = sys.argv[1]
output_file = sys.argv[2]

try:
    HOST = socket.gethostbyname(hostname)
except:
    print("Error: could not resolve hostname")
    exit(1)

PORT = 8888

try:
    f = open(output_file, "w")
except:
    print("Cannot write to file")
    exit(1)

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
    print("Error: could not create socket")
    exit(1)

try:
    client_socket.connect((HOST, PORT))
except:
    print("Error: could not connect to server")
    exit(1)

data = client_socket.recv(1024)
f.write(data.decode())
f.close()
client_socket.close()
