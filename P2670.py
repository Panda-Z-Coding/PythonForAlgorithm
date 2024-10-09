n, m = input().split()
n = int(n)
m = int(m)
arr = [[0 for _ in range(m)] for _ in range(n)]
if n == m == 1:
    i = input()
    print(i)
else:
    for i in range(n):
        s = input()
        if '*' in s:
            for j in range(len(s)):
                if s[j] == '*':
                    arr[i][j] = '*'
                    if i == 0 and j == 0:
                        if arr[i][j + 1] != '*':
                                arr[i][j + 1] += 1
                        if arr[i + 1][j] != '*':
                                arr[i + 1][j] += 1
                        if arr[i + 1][j + 1] != '*':
                                arr[i + 1][j + 1] += 1
                    elif i == 0 and j == m - 1:
                        if arr[i][j - 1] != '*':
                            arr[i][j - 1] += 1
                        if arr[i + 1][j] != '*':
                            arr[i + 1][j] += 1
                        if arr[i + 1][j - 1] != '*':
                            arr[i + 1][j - 1] += 1
                    elif i == n - 1 and j == 0:
                        if arr[i - 1][j] != '*':
                            arr[i - 1][j] += 1
                        if arr[i][j + 1] != '*':
                            arr[i][j + 1] += 1
                        if arr[i - 1][j + 1] != '*':
                            arr[i - 1][j + 1] += 1
                    elif i == n - 1 and j == m - 1:
                        if arr[i - 1][j] != '*':
                            arr[i - 1][j] += 1
                        if arr[i][j - 1] != '*':
                            arr[i][j - 1] += 1
                        if arr[i - 1][j - 1] != '*':
                            arr[i - 1][j - 1] += 1
                    elif i == 0 and j != 0 and j != m - 1:
                        if arr[i][j + 1] != '*':
                            arr[i][j + 1] += 1
                        if arr[i][j - 1] != '*':
                            arr[i][j - 1] += 1
                        if arr[i + 1][j] != '*':
                            arr[i + 1][j] += 1
                        if arr[i + 1][j - 1] != '*':
                            arr[i + 1][j - 1] += 1
                        if arr[i + 1][j + 1] != '*':
                            arr[i + 1][j + 1] += 1
                    elif i == n - 1 and j != 0 and j != m - 1:
                        if arr[i][j + 1] != '*':
                            arr[i][j + 1] += 1
                        if arr[i][j - 1] != '*':
                            arr[i][j - 1] += 1
                        if arr[i - 1][j] != '*':
                            arr[i - 1][j] += 1
                        if arr[i - 1][j - 1] != '*':
                            arr[i - 1][j - 1] += 1
                        if arr[i - 1][j + 1] != '*':
                            arr[i - 1][j + 1] += 1
                    elif j == m - 1 and i != 0 and i != n - 1:
                        if arr[i][j - 1] != '*':
                            arr[i][j - 1] += 1
                        if arr[i - 1][j] != '*':
                            arr[i - 1][j] += 1
                        if arr[i - 1][j - 1] != '*':
                            arr[i - 1][j - 1] += 1
                        if arr[i + 1][j] != '*':
                            arr[i + 1][j] += 1
                        if arr[i + 1][j - 1] != '*':
                            arr[i + 1][j - 1] += 1
                    elif j == 0 and i != 0 and i != n - 1:
                        if arr[i][j + 1] != '*':
                            arr[i][j + 1] += 1
                        if arr[i - 1][j] != '*':
                            arr[i - 1][j] += 1
                        if arr[i - 1][j + 1] != '*':
                            arr[i - 1][j + 1] += 1
                        if arr[i + 1][j] != '*':
                            arr[i + 1][j] += 1
                        if arr[i + 1][j + 1] != '*':
                            arr[i + 1][j + 1] += 1
                    else:
                        if arr[i][j + 1] != '*':
                            arr[i][j + 1] += 1
                        if arr[i][j - 1] != '*':
                            arr[i][j - 1] += 1
                        if arr[i + 1][j] != '*':
                            arr[i + 1][j] += 1
                        if arr[i - 1][j] != '*':
                            arr[i - 1][j] += 1
                        if arr[i - 1][j - 1] != '*':
                            arr[i - 1][j - 1] += 1
                        if arr[i - 1][j + 1] != '*':
                            arr[i - 1][j + 1] += 1
                        if arr[i + 1][j - 1] != '*':
                            arr[i + 1][j - 1] += 1
                        if arr[i + 1][j + 1] != '*':
                            arr[i + 1][j + 1] += 1
    for i in range(n):
        for j in range(m):
            print(arr[i][j],end='')
        print()

           
