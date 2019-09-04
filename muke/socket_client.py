import socket

client = socket.socket()

server_ip_port = ("127.0.0.1", 8889)

#连接服务器
client.connect(server_ip_port)

# 接受主机信息

data = client.recv(1024)

print(data.decode())

# 定义一个循环不断发送消息

while True:

    # 输入发送的消息
    msg_input = input("请输入发送的消息")
    client.send(msg_input.encode())

    if msg_input == 'exit':
        break

    data = client.recv(1024)
    print(data.decode())

    data = client.recv(1024)
    print(data.decode())