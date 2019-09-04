import random
import socket

# 创建实例
sk = socket.socket()

# 定义绑定ip port

ip_port = ("127.0.0.1", 8888)

# 绑定监听
sk.bind(ip_port)

# 最大连接数
sk.listen(5)
#提示信息

while True:

    print("正在进行等待接受数据。。。")
    # 接受数据
    conn , address = sk.accept()

    # 定义信息
    msg = "连接成功！"

    #返回
    # pythong3 以上，网络数据发送的都是byte类型， str类需要编码
    conn.send(msg.encode())

    while True:
        # 接受客户端发送的消息
        data = conn.recv(1024)
        print(data.decode())

        if data == b'exit':
            break

        # 处理客户端数据
        conn.send(data)
        conn.send(str(random.randint(1, 10000)).encode())
    conn.close()