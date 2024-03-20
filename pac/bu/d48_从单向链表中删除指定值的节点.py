"""
5 2 3 2 4 3 5 2 1 4 3

5:总的节点数
第一个2：表示首节点
3 2：3表示是第二个节点， 2表示 3是由上一个节点，也就是2衍生出来，就是通过节点2可以访问到节点3
"""

while True:
	try:
		inp_str = input().strip().split()
		# inp_str = ['5', '2', '3', '2', '4', '3', '5', '2', '1', '4', '3']
		# 节点数
		n = int(inp_str[0])
		# 首节点
		first_node = inp_str[1]
		# 要删除的节点
		del_node = inp_str[-1]
		# 筛选出首节点之后要操作的节点及指针数 ['3', '2', '4', '3', '5', '2', '1', '4']
		c_list = inp_str[2:-1]

		res = [first_node]

		for i in range(0, len(c_list), 2):
			# 要插入的元素
			a = c_list[i]
			# 插入元素的前一个元素
			b = c_list[i + 1]
			# 要插入元素前一个元素的位置 + 1 = 插入元素的位置
			j = res.index(b) + 1
			res.insert(j, a)
		# print(res)
		# 对处理好的列表删除目标元素 ['2', '5', '3', '4', '1'] =>['2', '5', '4', '1']
		res.remove(del_node)
		print(' '.join(res))
	except:
		break
