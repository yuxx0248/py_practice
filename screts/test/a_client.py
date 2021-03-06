import socket
import sys
from cryptography.fernet import Fernet

class CLIENT(object):
	def __init__(self, addr, port):
		self.addr = addr
		self.port = port
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def connect(self):
		self.socket.connect((self.addr, self.port))

	def send(self, data):
		self.socket.sendall(data)

	def recv(self):
		data = self.socket.recv(1024)
		print('Received data: ', repr(data))
		return data

def main():
	if len(sys.argv) != 3:
		print ("python client.py {addr} {as_port} {tgs_port}")
		exit(1);

	host = sys.argv[1]
	as_port = int(sys.argv[2])

	# a_as key
	with open("../key_store/a_as_key", "rb") as file:
		aas_key = file.read()

	# get key to tgs from as_server
	client = CLIENT(host, as_port)
	client.connect()
	client.send(b"This is client A calling as server yooo")

	data = client.recv()
	
	# decrypt key to tgs 
	f = Fernet(aas_key)
	dstr = data.decode() + 'this is a test string'
	tgs_key = f.decrypt(dstr.encode('utf-8'))
	print (tgs_key)

if __name__ == '__main__':
    main()
