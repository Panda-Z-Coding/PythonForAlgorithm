import sys

n = input()

num_list = list(map(int, input().split())) #! map函数转化类型

print(max(num_list) - min(num_list))

