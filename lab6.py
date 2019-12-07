from cryptography.fernet import Fernet
from AS import AS

message = "my deep dark secret".encode()

# The keys known
key_A_AS = Fernet.generate_key()
key_B_AS = Fernet.generate_key()
key_AS_TGS = Fernet.generate_key()

as_server = AS(key_A_AS, key_B_AS, key_AS_TGS, 'localhost', 50001)



# f = Fernet(key_A_AS)
# encrypted = f.encrypt(message)
# decrypted = f.decrypt(encrypted)

# print(message)
# print(encrypted)
# print(decrypted)
# print(message == decrypted)

# f = Fernet(key_B_AS)
# encrypted = f.encrypt(message)
# decrypted = f.decrypt(encrypted)

# print(message)
# print(encrypted)
# print(decrypted)
# print(message == decrypted)

# f = Fernet(key_AS_TGS)
# encrypted = f.encrypt(message)
# decrypted = f.decrypt(encrypted)

# print(message)
# print(encrypted)
# print(decrypted)
# print(message == decrypted)