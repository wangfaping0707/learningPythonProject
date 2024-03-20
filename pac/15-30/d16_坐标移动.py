list1 = input().strip().split(";")
n, m = 0, 0
for item in list1:
	if 2 <= len(item) <= 3 and item[0] in ["A", "D", "W", "S"] and item[1:].isdigit():
		num = int(item[1:])
		if item[0] == "A":
			n = n - num
		elif item[0] == "D":
			n = n + num
		elif item[0] == "W":
			m = m + num
		elif item[0] == "S":
			m = m - num

print(str(n) + ',' + str(m))
