n = int(input())

puke = list()

for _ in range(n):
    s = input()
    puke.append(s)

puke = set(puke)
puke = list(puke)
l = len(puke)
print(52 - l)
