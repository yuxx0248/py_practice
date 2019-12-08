import socket

class SERVER(object):
    def __init__(self, addr, port):
        self.svr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.svr.bind((addr, port))
        self.svr.listen(1)

    def serve(self):
        while True:
            conn, addr = self.svr.accept()
            from_client = ''
 
            while True:
                data = conn.recv(4096)
                if not data: break
                from_client += data
                print ("from_client")
 
                conn.send("I am SERVER\n")
 
        conn.close()
        print ("client disconnected")
