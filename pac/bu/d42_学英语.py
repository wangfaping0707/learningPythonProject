"""
six hundred and twenty three billion five hundred and sixty five million one hundred and sixty one thousand two hundred and twenty five
数字： 623      565       161         225
      billion  million   thousand    hundred
million = 一百万 1000000
billion = 十亿   1000000000

"""
num1 = [' ', ' one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
        'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
num2 = [' ', ' ', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def trans_num(n):
	if n < 20:
		return num1[n]
	elif n < 100:
		return num2[n // 10] + ' ' + num1[n % 10]
	elif n == 100:
		return num1[n // 100] + ' ' + 'hundred'
	elif n < 1000:
		return num1[n // 100] + ' ' + 'hundred and' + ' ' + trans_num(n % 100)
	elif n < 1000000:
		return trans_num(n // 1000) + ' ' + 'thousand' + '' + trans_num(n % 1000)
	elif n < 1000000000:
		return trans_num(n // 1000000) + ' ' + 'million' + ' ' + trans_num(n % 1000000)
	elif n < 1000000000000:
		return trans_num(n // 1000000000) + ' ' + 'billion' + ' ' + trans_num(n % 1000000000)


while True:
	try:
		data = int(input().strip())
		if data == 0:
			print('zero')
		else:
			print(trans_num(data).strip())
	except:
		break
