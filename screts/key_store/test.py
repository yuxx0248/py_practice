import sys
from cryptography.fernet import Fernet

with open("a_as_key", "r") as file:
    public_key = file.read()

f = Fernet(public_key)
message = b"leroy jenkins!"
encrypted = f.encrypt(message)

print ("encryped message", encrypted)

ff = Fernet(public_key)
decryped = ff.decrypt(encrypted)

print ("decryped message", decryped)

if message == decryped:
	print ("match")
else:
	print ("shit")
