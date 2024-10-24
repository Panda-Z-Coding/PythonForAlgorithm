n = int(input())

arr = list(map(int, input().split()))
ans = [0] 
ans[0] = arr[0]
for i in range(1,n):
    if arr[i] in ans:
        pass
    else:
        ans.append(arr[i])
ans.sort()
print(len(ans))
print(' '.join(map(str, ans)))