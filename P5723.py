"""
质数口袋
"""

def is_Prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True
    
        

# l = int(input())

# sum_num = 0
# num = 1
# count = 0
# while sum_num <= l:
#     num += 1
#     if is_Prime(num):
#         sum_num += num
#         if sum_num <= l:
#             print(num)
#             count += 1


print(is_Prime(10301))
#! AC