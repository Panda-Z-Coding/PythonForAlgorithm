'''
阶乘之和:递归
'''

def factorial_num(n):
    if(n != 0):
        return n * factorial_num(n - 1)
    else:
        return 1
def sum_fac_num(n):
    sum = 0
    for i in range(1,n + 1):
        sum += factorial_num(i)
    return sum

n = int(input())
print(sum_fac_num(n))

# AC
