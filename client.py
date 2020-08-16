from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import json

HOST = ''
PORT = 4000

socket = socket(AF_INET, SOCK_STREAM)

class Client:

    def __init__(self,  HOST, PORT, socket):
        self.HOST = HOST
        self.PORT = PORT
        self.socket = socket


    print(f'Client is {HOST} and port is {PORT}')
    #function connects client socket to HOST, PORT and listen buffer from connection
    def connection(self):
        self.socket.connect((HOST, PORT))
        self.listen()
        print('Connecting...')

    def listen(self):
        thread = Thread(target=self.listen_thread)
        thread.start()
    
    def listen_thread(self):
        while True:
            data = json.loads(self.socket.recv(4096).decode('utf-8'))
            if 'chat' in data.keys():
                print('>>>>>>> {}'.format(data['chat']))
    #function sends message to the connected socket, (Server)
    def send(self, msg, function):
        data = {function: msg}
        #converts to json
        msg = json.dumps(data)
        self.socket.sendall(msg.encode('utf-8'))

    def reply(self):  
        print("---messages---")
        while True:
            msg = input()
            response = self.send(msg, 'chat')





