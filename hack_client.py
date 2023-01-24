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
sock.connect((args.target, int(args.port)))

while True:
	command = input("Console #> ")
	sock.send(command.encode())
	result = sock.recv(1024).decode()
	print(result)
