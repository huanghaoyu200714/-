import socket
from threading import Thread
def client_send(client):
    while 1:
        msg = input('请输入消息:')
        client.send(msg.encode())

def client_receive(client):
    while 1:
        msg = client.recv(1460)
        print('收到服务器发送过来的消息:', msg.decode())

def start():
    t1 = Thread(target=client_send, args=(client,))
    t2 = Thread(target=client_receive, args=(client,))
    t1.start()
    t2.start()

if __name__ == "__main__":
    client = socket.socket()
    client.connect(('127.0.0.1', 5229))
    start()