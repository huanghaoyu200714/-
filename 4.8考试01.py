import socket
from concurrent.futures import ThreadPoolExecutor
import threading

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
    pool = ThreadPoolExecutor(128)
    lock = threading.Lock()
    while 1:
        lock.acquire()                  #ss为全局变量，需要加锁避免不同线程对其值造成影响
        conn, addr = ss.accept()
        lock.release()
        list1.append(conn)
        print('{}已经加入'.format(addr))
        pool.submit(handle_conn, conn, addr)



if __name__ == "__main__":
    addr = ("127.0.0.1", 5229)
    conn_sever(addr)
