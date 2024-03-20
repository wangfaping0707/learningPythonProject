import socket

# 1.买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.拨通服务电话
phone.connect(('127.0.0.1', 8080))

# 3.通信
while True:
	msg = input('输入要发送的信息>>>:').strip()
	if len(msg) == 0:
		continue
	phone.send(msg.encode('utf-8'))
	data = phone.recv(1024)
	print(data.decode('utf-8'))

# 4、关闭链接，必须要进行的操作
phone.close()
