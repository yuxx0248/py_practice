import socket
import sys

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
		print('Received', repr(data))


def main():
	if len(sys.argv) != 3:
		print ("python client.py {addr} {port}")
		exit(1);

	host = sys.argv[1]
	port = int(sys.argv[2])

	client = CLIENT(host, port)
	client.connect()
	client.send(b"WHAT A PILE OF SHIT")
	client.recv()

if __name__ == '__main__':
    main()