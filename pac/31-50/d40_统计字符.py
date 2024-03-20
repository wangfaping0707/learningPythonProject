
str = input()

num_arr = []
alpha_arr = []
space_arr = []
others = []

for i in str:
	if i.isdigit():
		num_arr.append(i)
	elif i.isalpha():
		alpha_arr.append(i)
	elif i.isspace():
		space_arr.append(i)
	else:
		others.append(i)

print(len(alpha_arr))
print(len(space_arr))
print(len(num_arr))
print(len(others))




