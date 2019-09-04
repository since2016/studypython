import socket

ip_port = ("127.0.0.1", 8888)
# 定义实例
sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


while True:
    # 输入需要发送到消息
    msg_input = input("输入需要发送的消息")
    # 退出的条件
    if msg_input == 'exit':
        break

    sk.sendto(msg_input.encode(),ip_port)

# 发送关闭信息
sk.close()