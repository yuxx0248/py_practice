import socket

class SERVER(object):
    def __init__(self, addr, port):
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
 
 				# return other stuff in return
                conn.send(data)
 
        conn.close()
        print ("client disconnected")

def main():
    server = SERVER('localhost', 50051)
    server.serve()

if __name__ == '__main__':
    main()