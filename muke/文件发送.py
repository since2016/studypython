import socket

sk = socket.socket()

# 定义连接端口
ip_port = ('127.0.0.1', 9999)

# 服务器连接

sk.connect(ip_port)


# 打开文件
with open('socket_client.py','rb') as f:
    # 每一段分割文件
    for i in f:
        sk.send(i)
        data = sk.recv(1024)
        if data == b'success':
            continue

# 给服务器端发送结束信号
sk.send('quit'.encode())