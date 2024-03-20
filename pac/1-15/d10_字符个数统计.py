def count_char(str):
	string = ''.join(set(str))
	count = 0
	for i in string:
		if ord(i) >= 1 and ord(i) <= 127:
			count += 1
	return count


print(count_char(input().strip()))
