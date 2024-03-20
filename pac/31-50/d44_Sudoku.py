# num_arr = []
#
# for i in range(9):
# 	num_arr.append(list(map(int, input().strip().split())))
#
#

m = [[0, 9, 2, 4, 8, 1, 7, 6, 3],
     [4, 1, 3, 7, 6, 2, 9, 8, 5],
     [8, 6, 7, 3, 5, 9, 4, 1, 2],
     [6, 2, 4, 1, 9, 5, 3, 7, 8],
     [7, 5, 9, 8, 4, 3, 1, 2, 6],
     [1, 3, 8, 6, 2, 7, 5, 9, 4],
     [2, 7, 1, 5, 3, 8, 6, 4, 9],
     [3, 8, 6, 9, 1, 4, 2, 5, 7],
     [0, 4, 5, 2, 7, 6, 8, 3, 1]]

all_n = {1, 2, 3, 4, 5, 6, 7, 8, 9}

row = [m[0][j] for j in range(9)]
col = [m[i][0] for i in range(9)]
print(f'row:{row}')
print(f'col:{col}')

x = 1
y = 0
# box = [m[i][j] for i in range((x // 3) * 3, (x // 3) * 3 + 3) for j in
#        range((y // 3) * 3, (y // 3) * 3 + 3)]

box = []
for i in range((x // 3) * 3, (x // 3) * 3 + 3):
	for j in range((y // 3) * 3, (y // 3) * 3 + 3):
		box.append(m[i][j])
print(f'box:{box}')

value = list(all_n - set(row) - set(col) - set(box))


all_n = {5}











"""
0 9 2 4 8 1 7 6 3
4 1 3 7 6 2 9 8 5
8 6 7 3 5 9 4 1 2
6 2 4 1 9 5 3 7 8
7 5 9 8 4 3 1 2 6
1 3 8 6 2 7 5 9 4
2 7 1 5 3 8 6 4 9
3 8 6 9 1 4 2 5 7
0 4 5 2 7 6 8 3 1
"""
