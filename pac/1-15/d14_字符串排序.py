counts = int(input().strip())
list1 = []
for i in range(counts):
	str = input().strip()
	list1.append(str)
list1.sort()
for i in list1:
	print(i, end='\n')
