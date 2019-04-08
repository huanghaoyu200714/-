import socket
from threading import Thread
list1 = []
def handle_conn(conn, addr):
    while 1:
        msg = conn.recv(6553)
        return_msg = '地址是{}的用户说{}'.format(addr, msg.decode())
        for co in list1:
            co.send(return_msg.encode())


def conn_sever(addr):
    ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ss.bind(addr)
    ss.listen()
    print('服务器已经开启')
    while 1:
        conn, addr = ss.accept()
        list1.append(conn)
        print('{}已经加入'.format(addr))
        handle = Thread(target=handle_conn, args=(conn, addr))
        handle.start()


if __name__ == "__main__":
    addr = ("127.0.0.1", 5229)
    conn_sever(addr)
