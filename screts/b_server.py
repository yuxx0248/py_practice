import socket
import sys
from cryptography.fernet import Fernet

class SERVER(object):
    def __init__(self, addr, port, btgs_key):
        self.btgs_key = btgs_key
        self.svr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.svr.bind((addr, port))
        self.svr.listen(1)

    def serve(self):
        while True:
            conn, addr = self.svr.accept() 
            while True:
                data = conn.recv(4096)
                if not data: break

                print ("B SERVER:: ", data)

                f = Fernet(self.btgs_key)
                message = "B SERVER: You have finally reached B!"
                data = f.encrypt(message.encode('utf-8'))

                conn.send(data) 
        conn.close()
        print ("client disconnected")

def main():
    if len(sys.argv) != 3:
        print ("python server.py {addr} {port}")
        exit(1);

    addr = sys.argv[1]
    port = int(sys.argv[2])
   
    # b_tgs key
    with open("key_store/b_tgs_key", "rb") as file:
        btgs_key = file.read()

    server = SERVER(addr, port, btgs_key)
    server.serve()

if __name__ == '__main__':
    main()
