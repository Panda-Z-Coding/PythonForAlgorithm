# n = int(input())
# #! 创建二维数组 -- 列表推导式
# Magic_square = [[0 for _ in range(n)] for _ in range(n)]
# #首先将 1 写在第一行的中间
# Magic_square[0][n // 2] = 1

# #获取上一个安放 K的位置
# pre_pos = [0, n // 2]
# #按如下方式从小到大依次填写每个数 K(K=2,3,⋯,N×N)
# for k in range(2,n*n + 1):
#     #1.若 (K−1)在第一行但不在最后一列，则将 K 填在最后一行， (K−1)所在列的右一列
#     if pre_pos[0] == 0 and pre_pos[1] != n - 1:
#         Magic_square[n - 1][pre_pos[1] + 1] = k
#         #更新前一个坐标
#         pre_pos[0] = n - 1
#         pre_pos[1] = pre_pos[1] + 1
#     if pre_pos[1] == n - 1 and pre_pos[0] != 0:
#         Magic_square[pre_pos[0] - 1][0] = k
#         pre_pos[0] = pre_pos[0] - 1
#         pre_pos[1] = 0
#     if pre_pos[0] == 0 and pre_pos[1] == n - 1:
#         Magic_square[pre_pos[0] - 1][pre_pos[1]] = k
#         pre_pos[0] = pre_pos[0] - 1
#         pre_pos[1] = pre_pos[1]
#     if pre_pos[0] != 0 and pre_pos[1] != n-1:
#         if Magic_square[pre_pos[0] - 1][pre_pos[1] + 1] == 0:
#             Magic_square[pre_pos[0] - 1][pre_pos[1] + 1] = k
#             pre_pos[0] = pre_pos[0] - 1
#             pre_pos[1] = pre_pos[1] + 1
#         else:
#             Magic_square[pre_pos[0] - 1][pre_pos[1]] = k
#             pre_pos[0] = pre_pos[0] - 1
#             pre_pos[1] = pre_pos[1]

# print(Magic_square)

n = int(input())

# 创建二维数组 -- 列表推导式
Magic_square = [[0 for _ in range(n)] for _ in range(n)]

# 首先将 1 写在第一行的中间
Magic_square[0][n // 2] = 1

# 获取上一个安放 K 的位置
pre_pos = [0, n // 2]

# 按如下方式从小到大依次填写每个数 K(K=2,3,⋯,N*N)
for k in range(2, n*n + 1):
    # 计算新位置
    new_i = (pre_pos[0] - 1) % n
    new_j = (pre_pos[1] + 1) % n
    
    # 如果新位置已经被填充，则调整到下一个位置
    if Magic_square[new_i][new_j] != 0:
        new_i = (pre_pos[0] + 1) % n
        new_j = pre_pos[1]
    
    # 将 K 填入新的位置
    Magic_square[new_i][new_j] = k
    
    # 更新前一个坐标
    pre_pos = [new_i, new_j]

# 打印魔方阵
for row in Magic_square:
    print(" ".join(str(x) for x in row))
