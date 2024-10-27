'''
暴力模拟


'''

N, Na, Nb = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

ScoreA = 0
ScoreB = 0

# 用取模运算循环遍历出圈的数组
#

# for i in range(N):
#     if A[(i + Na) % Na] == 0 and B[(i + Nb) % Nb] == 0:
#         # 剪刀对剪刀
#         pass
#     if A[(i + Na) % Na] == 0 and B[(i + Nb) % Nb] == 1:
#         # 剪刀对石头
#         ScoreB += 1
#         pass
#     if A[(i + Na) % Na] == 0 and B[(i + Nb) % Nb] == 2:
#         # 剪刀对布
#         ScoreA += 1
#         pass
#     if A[(i + Na) % Na] == 0 and B[(i + Nb) % Nb] == 3:
#         # 剪刀对蜥蜴人
#         ScoreA += 1
#         pass
#     if A[(i + Na) % Na] == 0 and B[(i + Nb) % Nb] == 4:
#         # 剪刀对博斯克
#         ScoreB += 1
#         pass
#     if A[(i + Na) % Na] == 1 and B[(i + Nb) % Nb] == 0:
#         # 石头对剪刀
#         ScoreA += 1
#         pass
#     if A[(i + Na) % Na] == 1 and B[(i + Nb) % Nb] == 1:
#         # 石头对石头
#         pass
#     if A[(i + Na) % Na] == 1 and B[(i + Nb) % Nb] == 2:
#         # 石头对布
#         ScoreB += 1
#         pass
#     if A[(i + Na) % Na] == 1 and B[(i + Nb) % Nb] == 3:
#         # 石头对蜥蜴人
#         ScoreA += 1
#         pass
#     if A[(i + Na) % Na] == 1 and B[(i + Nb) % Nb] == 4:
#         # 石头对博斯克
#         ScoreB += 1
#         pass
#     if A[(i + Na) % Na] == 2 and B[(i + Nb) % Nb] == 0:
#         # 布对剪刀
#         ScoreB += 1
#     if A[(i + Na) % Na] == 2 and B[(i + Nb) % Nb] == 1:
#         # 布对石头
#         ScoreA += 1
#         pass
#     if A[(i + Na) % Na] == 2 and B[(i + Nb) % Nb] == 2:
#         # 布对布
#         pass
#     if A[(i + Na) % Na] == 2 and B[(i + Nb) % Nb] == 3:
#         # 布对蜥蜴人
#         ScoreB += 1
#         pass
#     if A[(i + Na) % Na] == 2 and B[(i + Nb) % Nb] == 4:
#         # 布对bosike
#         ScoreA += 1
#         pass
#     if A[(i + Na) % Na] == 3 and B[(i + Nb) % Nb] == 0:
#         #
#         ScoreB += 1
#         pass
#     if A[(i + Na) % Na] == 3 and B[(i + Nb) % Nb] == 1:
#         #
#         ScoreB += 1
#         pass
#     if A[(i + Na) % Na] == 3 and B[(i + Nb) % Nb] == 2:
#         #
#         ScoreA += 1
#         pass
#     if A[(i + Na) % Na] == 3 and B[(i + Nb) % Nb] == 3:
#         #
#         pass
#     if A[(i + Na) % Na] == 3 and B[(i + Nb) % Nb] == 4:
#         #
#         ScoreA += 1
#         pass
#     if A[(i + Na) % Na] == 4 and B[(i + Nb) % Nb] == 0:
#         #
#         ScoreA += 1
#         pass
#     if A[(i + Na) % Na] == 4 and B[(i + Nb) % Nb] == 1:
#         #
#         ScoreA += 1
#         pass
#     if A[(i + Na) % Na] == 4 and B[(i + Nb) % Nb] == 2:
#         #
#         ScoreB += 1
#         pass
#     if A[(i + Na) % Na] == 4 and B[(i + Nb) % Nb] == 3:
#         #
#         ScoreB += 1
#         pass
#===屎山代码===#

# 用数组模拟
# 甲获胜 -> 1 相反就 -1
score = [
    [0, -1, 1, 1, -1],
    [1, 0, -1, 1, -1],
    [-1, 1, 0, -1, 1],
    [-1, -1, 1, 0, 1],
    [1, 1, -1, -1, 0]
]

for i in range(N):
    if score[A[(i + Na) % Na]][B[(i + Nb) % Nb]] == 1:
        ScoreA += 1
    elif score[A[(i + Na) % Na]][B[(i + Nb) % Nb]] == 0:
        pass
    else:
        ScoreB += 1
    
print(f"{ScoreA} {ScoreB}")
