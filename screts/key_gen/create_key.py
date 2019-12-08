import sys
from cryptography.fernet import Fernet

if len(sys.argv) != 2:
	print ("python client {token name}")
	exit(1);

name = sys.argv[1]

# generate public key and private key
key = Fernet.generate_key()

key_file = open(name + "_key", "w+")
key_file.write(key.decode('utf-8'))
