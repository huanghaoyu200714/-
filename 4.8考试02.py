import socket
from concurrent.futures import ThreadPoolExecutor
import sys
def client_send(client):
    while 1:
        msg = input('请输入消息:')
        if msg == '退出聊天室':
            client.send(msg.encode())
            print('你已经退出')
            sys.exit()
        client.send(msg.encode())

def client_receive(client):
    while 1:
        msg = client.recv(1460)
        print('收到服务器发送过来的消息:', msg.decode())

def start():
    pool = ThreadPoolExecutor(128)
    pool.submit(client_send, client)
    pool.submit(client_receive, client)


if __name__ == "__main__":
    client = socket.socket()
    client.connect(('127.0.0.1', 5229))
    start()