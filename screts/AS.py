import pickle
import socket
import sys

BUF_SZ = 1024  # tcp receive buffer size
BACKLOG = 12

class AS(object):
    def __init__(self, addr, port):
        # self.key_a_as = a
        # self.key_b_as = b
        # self.key_as_tgs = c
        self.listener = self.start_a_server(addr, port)


    @staticmethod
    def start_a_server(addr, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((addr, port))
        listener.listen(1)
        return listener

#     def run(self, addr, port):
#         print('AS is on ({}, {})'.format(addr, port))
#         while True:
#             try:
#                 peer, address = self.listener.accept() 
                # 
# 
#             except Exception as err:
#                 print('accept failed {}'.format(err))   

    def receive_message(self, peer, addr):
        while True:
            try:
                data = peer.recv(BUF_SZ)
                if not data:
                    raise ValueError('socket closed')
                msg = pickle.loads(data)
                print('Listerner received request msg: ', msg)
                response('hello')
            except:
                peer.close()
                return False

    def response(msg):
        response = ''

        # if msg == 'find_successor':
        #     print('\nRequest - find_successor')
        #     response = self.find_successor(info_1)

        # elif msg == 'successor':
        #     print('\nRequest - successor')
        #     response = self.finger[1].node

        # elif msg == 'closest_preceding_finger':
        #     print('\nRequest - closest_preceding_finger')
        #     response = self.closest_preceding_finger(info_1)

        # elif msg == 'find_predecessor':
        #     print('\nRequest - find_predecessor')
        #     response = self.find_predecessor(info_1)

        # elif msg == 'set_predecessor':
        #     print('\nRequest - set_predecessor')
        #     response = self.set_predecessor(info_1)

        # elif msg == 'update_finger_table':
        #     print('\nRequest - update_finger_table')
        #     response = self.update_finger_table(info_1, info_2)

        # elif msg == 'update_keys':
        #     print('\nRequest - update_keys')
        #     response = self.update_keys(info_1)

        print("Response with msg: ", msg)
        peer.sendall(pickle.dumps(msg))

def main():
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket.bind(('localhost', 50001)
    socket.listen(1)
    print("init auth server")
    conn, addr = as_server.listener.accept()
    print("got connection")

if __name__ == '__main__':
    main()