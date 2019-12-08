import socket
import sys
from cryptography.fernet import Fernet

class SERVER(object):
    def __init__(self, addr, port, astgs_key):
        self.astgs_key = astgs_key
        self.svr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.svr.bind((addr, port))
        self.svr.listen(1)

    def serve(self):
        while True:
            conn, addr = self.svr.accept() 
            while True:
                data = conn.recv(4096)
                if not data: break

                print (data)

                f = Fernet(self.astgs_key)
                data = f.encrypt(data)

                conn.send(b"this is tgs") 
        conn.close()
        print ("client disconnected")

def main():
    if len(sys.argv) != 3:
        print ("python server.py {addr} {port}")
        exit(1);

    addr = sys.argv[1]
    port = int(sys.argv[2])
   
    # as_tgs key
    with open("key_store/as_tgs_key", "rb") as file:
        astgs_key = file.read()

    server = SERVER(addr, port, astgs_key)
    server.serve()

if __name__ == '__main__':
    main()
