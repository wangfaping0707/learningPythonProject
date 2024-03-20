from decimal import Decimal
from fractions import Fraction

print(0.1 + 0.1 + 0.1 - 0.3)

num = Decimal('0.1') + Decimal('0.10') + Decimal('0.100') - Decimal('0.3000')
print('num的类型是：', type(num))
print('打印num的数字：', num)

print('----------------------------------------------------------')
num1 = Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3)
print('num1的类型是：', type(num1))
print('打印num1的数字：', num1)

print('***********************************************************')

x = Fraction(1, 3)
y = Fraction(5, 6)

print(x)
print(y)

print('加法：', x + y)
print('减法：', x - y)
print('乘法：', x * y)
print('除法：', x / y)


import decimal
decimal.getcontext().prec = 2
print(Decimal(1) / Decimal(3))














