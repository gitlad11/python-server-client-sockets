from socket import socket, AF_INET, SOCK_STREAM
import time, datetime
import asynchat ,asyncore
import os
import threading
# server settings
PORT = 4000
ADDR = '127.0.0.1'
#AF_NET , SOCK_STREAM is socket's extension
socket  = socket(AF_INET, SOCK_STREAM)
socket.bind((ADDR,PORT))
conn_list = []
addr_list = []

#server initialization
def server(self, socket , conn_list , addr_list):
    self.socket = socket
    self.conn_list = conn_list
    self.addr_list = addr_list


#handle client's activity , sending messages
def client_handler(self, conn, address, conn_list, server):
    conn_time = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M')
    print(f'New connection at {conn_time}')
    print(f'{address} has been connected.')
    conn_establish = True
    #1024 is buffersize , after connection and conn_establish = true, get message from client and decode in utf-8
    while conn_establish:
        message = conn.recv(1024).decode('utf-8')
        #if client didn't send any messages break this function and rerun
        if not message:
            break
        #for clients in conn_list if socket is not server , then send message to all(broadcast)
    for conn in conn_list:
        if socket != server.socket:
            try:
                socket.sendall(message)
                #if client disconect socket close then remove client from conn_list
            except:
                socket.close()
                conn_list.remove(socket)


#start server 
def start():
    socket.listen()
    print("Waiting for connections")
    while True:
        try:
            conn , addr = socket.accept()
            conn_list.append(conn)
            addr_list.append(addr)
            #threding rerun function with given args 
            Thread = threading.Thread(target=client_handler, args=(conn , addr))
            Thread.start()
        except Exception as e:
            print(e)
            break


if __name__ == '__main__':
    start()






