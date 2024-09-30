n = int(input())
change_list = list()

while n != 1:
    if n % 2 == 0:
        change_list.append(n)
        n //= 2
    else:
        change_list.append(n)
        n = n * 3 + 1
change_list.append(1)
s = change_list[::-1]
ans = " ".join(map(str, s))
print(ans)
