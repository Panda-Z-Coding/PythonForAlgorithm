n = input()

score = list(map(int, input().split()))
s = sorted(score)
del s[-1]
del s[0]

print("{:.2f}".format(sum(s) / len(s)))