# 二叉树的中序遍历
n1 = list(map(int, input().strip().split()))

# 二叉树的前序遍历
n2 = list(map(int, input().strip().split()))

# 新二叉树的根节点值
new_node = sum(n1[:-1]) + sum(n2[:-1])
print(new_node)

"""
-3 12 6 8 9 -10 -7
8 12 -3 6 -10 9 -7
"""