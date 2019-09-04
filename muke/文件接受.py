import socket

sk = socket.socket()

# 定义连接端口
ip_port = ('127.0.0.1', 9999)

# 绑定端口
sk.bind(ip_port)

#最大连接数
sk.listen(5)

while True:
    # 等待客户端连接
    conn, address = sk.accept()

    # 要一直使用当前连接， 知道结束标准
    while True:
        with open('file','ab') as f:
            data = conn.recv(1024)
            if data == b'quit':
                break

            f.write(data)
        # 接受完成标志
        conn.send("success".encode())
        f.close()
    print("文件接收完成")

sk.close()