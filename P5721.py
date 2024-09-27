'''
数字直角三角形
'''

n = int(input())
a = 1
for i in range(1,n+1):
    for j in range(1,n - i + 2):
        print("{:02d}".format(a),end='')
        a += 1
    print()