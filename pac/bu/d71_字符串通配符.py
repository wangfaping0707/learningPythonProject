import re

pattern = input().strip().lower()
data = input().strip().lower()

pattern = pattern.replace('.', '\.').replace('?', '[a-z0-9]{1}').replace('*', '[a-z0-9]*')
if re.findall(pattern, data):
	print('true')
else:
	print('false')



# import re
# rule = input().strip().lower()
#
# s2 = input().strip().lower()
#
# rule = rule.replace('?', '[a-zA-Z0-9]{1}').replace('*', '[a-zA-Z0-9]*').replace('.', '\.')
# if s2 in re.findall(rule, s2):
# 	s = re.findall(rule, s2)
# 	print(s)
# 	print('true')
# else:
# 	print('false')