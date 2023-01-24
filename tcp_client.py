import socket

ip = input("[+] Input IP of the server : ")
port = int(input("[+] Input port of the server : "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))

while True:
	mess = input("[+] Input your message : ").encode()
	client.send(mess)
	response = client.recv(1024)
	print(f"[+] Response : {response.decode('utf-8')}")