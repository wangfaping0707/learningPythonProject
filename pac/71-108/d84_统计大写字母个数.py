import re

str = input().strip()

count = 0
for i in str:
	if re.search(r'[A-Z]', i):
		count += 1
print(count)

print('======================================')
while True:
	try:
		n = input()
		c = ''
		for i in n:
			if 'A' <= i <= 'Z':
				c += i
		print(len(c))
	except:
		break
