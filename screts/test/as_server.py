import socket
import sys
from cryptography.fernet import Fernet

class SERVER(object):
    def __init__(self, addr, port, aas_key):
        self.aas_key = aas_key
        self.svr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.svr.bind((addr, port))
        self.svr.listen(1)

    def serve(self):
        while True:
            conn, addr = self.svr.accept() 
            while True:
                data = conn.recv(4096)
                if not data: break

                print ("AS SERVER: recv: ", data)

                new_key = Fernet.generate_key()
                f = Fernet(self.aas_key)
                data = f.encrypt(new_key)

                conn.send(data)
                print ("AS SERVER: key for talking to tgs sent to client")
        conn.close()
        print ("client disconnected")

def main():
    if len(sys.argv) != 3:
        print ("python server.py {addr} {port}")
        exit(1);

    addr = sys.argv[1]
    port = int(sys.argv[2])

    # a_as key
    with open("../key_store/a_as_key", "rb") as file:
        aas_key = file.read()

    server = SERVER(addr, port, aas_key)
    server.serve()

if __name__ == '__main__':
    main()
