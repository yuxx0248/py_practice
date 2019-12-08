import socket
import sys
from z_service_registry_struct import REGISTRY
from cryptography.fernet import Fernet

class SERVER(object):
    def __init__(self, addr, port, astgs_key):
        self.astgs_key = astgs_key
        self.svr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.svr.bind((addr, port))
        self.svr.listen(1)

        self.registry = dict()

    def serve(self):
        # display all saved service registries
        print (self.registry)

        while True:
            conn, addr = self.svr.accept() 
            while True:
                data = conn.recv(4096)
                if not data: break
                
                service_name = data.decode()
                print ("TGS SERVER: Looking for service", service_name)
                if service_name in self.registry:
                    print ("TGS SERVER: found service regisry")
                    reg = self.registry[service_name]
                    path_to_key = ("key_store/" + reg.name + "_"
                        + reg.registry_service_name + "_key" )
                    print ("TGS SERVER: service key under: ", path_to_key)
                    message = path_to_key + "," + str(reg.port)

                    f = Fernet(self.astgs_key)
                    data = f.encrypt(message.encode('utf-8'))
                    conn.send(data)
                else:   
                    conn.send(b"the service you looking for is not registered")

        conn.close()
        print ("client disconnected")

    def register(self, register):
        self.registry[str(register.name)] = register

def loadSavedRegistry(server):
    service_b = REGISTRY(50053, "b", "tgs")
    server.register(service_b)

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
    loadSavedRegistry(server)
    server.serve()

if __name__ == '__main__':
    main()

