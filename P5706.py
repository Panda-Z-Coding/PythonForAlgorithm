t, n = input().split() #split()默认用空格和换行符分割，然后顺序赋值给两个变量
ans = float(t) / int(n)
a = "{:.3f}".format(ans)
print(a)
print(int(n)*2)