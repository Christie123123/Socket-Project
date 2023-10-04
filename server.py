import sys,os,socket
import threading

if len(sys.argv) != 2:
    print("Usage: python server.py <input file>")
    exit(1)

input_file = sys.argv[1]

try:
    f = open(input_file, "r")
    data = f.read()
except:
    print("Error: could not open file")
    exit(1)

if len(data) > 80:
    print("Error: file too large")
    exit(1)

# Define the host and port
HOST = 'localhost'
PORT = 8888

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
    print("Error: could not create socket")
    exit(1)

# Bind the socket to the host and port
try:
    server_socket.bind((HOST, PORT))
except:
    print("Error: could not bind socket")
    exit(1)
# Listen for incoming connections
server_socket.listen(1)
# Wait for a client to connect


def handle_client(client_socket):
    client_socket.send(data.encode())
    client_socket.close()

while True:
    client_socket, client_address = server_socket.accept()
    print("Connection from: " + str(client_address))
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()

# Close the socket
server_socket.close()