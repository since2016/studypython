import socketserver
import random


# 定义一个类

class myServer(socketserver.BaseRequestHandler):

    # 如果handle 方法报错， 则会跳过，
    # setup finish 仍会执行
    # 先执行setup
    def setup(self):
        pass

    # 再执行handle
    def handle(self):
        # 定义连接变量
        conn = self.request
        msg = "Hello World"
        conn.send(msg.encode())
        while True:
            data = conn.recv(1024)

            print(data.decode())
            if data == b'exit':
                break;

            conn.send(data.encode())
            conn.send(str(random.randint(1,1000).enode()))

    # 最后执行
    def finish(self):
        pass


if __name__ == '__main__':
    # 创建多线程实例
    server  = socketserver.ThreadingTCPServer(("127.0.0.1", 8889), myServer)

    # 开启异步多线程，等待连接，
    server.serve_forever()