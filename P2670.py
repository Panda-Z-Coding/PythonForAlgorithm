n, m = input().split()
n = int(n) #! 行列不分！！！
m = int(m)
arr = [[0 for _ in range(105)] for _ in range(105)]
"""
输入时候如果遇到*就在附近的八个各自加一,然后输出的时候遇到*就按*输出
"""
for i in range(1,n+1):
    s = input()
    for j in range(len(s)):
        if s[j] == '*':
            arr[i][j+1] = -1000
            #! j+1 是*所在的点
            arr[i][j+2] += 1
            arr[i][j] += 1
            arr[i-1][j+1] += 1
            arr[i-1][j] += 1
            arr[i-1][j+2] += 1
            arr[i+1][j+1] += 1
            arr[i+1][j] += 1
            arr[i+1][j+2] += 1

for i in range(1,n+1):
    for j in range(1,m+1):
        if arr[i][j] < 0:
            print('*',end='')
            continue
        print(arr[i][j],end='')
    print()

           
# AC 