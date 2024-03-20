import socket

# 1、买手机, SOCK_STREAM   流式协议=》tcp协议
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2、绑定手机卡,  0 —— 65535， 1024以前的都被系统保留使用
phone.bind(('127.0.0.1', 8080))

# 3、开机, backlog=5 指的是半链接池的大小
phone.listen(5)

# 4、等待打电话链接请求   conn就是tcp三次握手建立的手法消息的通道对象
conn, client_addr = phone.accept()
print(conn)
print(f'客户端的ip和端口:{client_addr}')

# 5、基于建立的通道进行通信:收/发消息: 最大接收的数据为1024Bytes,收到的是bytes类型
while True:
	try:
		data = conn.recv(1024)
		if len(data) == 0:
			# 在unix系统中，一旦data收到的是空，意味着是一种异常的行为：客户端非法断开了链接
			break
		print('客户端发来的消息:', data.decode('utf-8'))
		conn.send(data.upper())
	except Exception:
		# 针对的是windows系统
		break

# 6、关闭电话链接conn,必须要进行的操作
conn.close()

# 7、可选操作:关机
# phone.close()
