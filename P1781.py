
n = int(input())
current_max = 0
number = 1
for i in range(1,n+1):
    num = int(input())
    if num > current_max:
        current_max = num
        number = i
print(number)
print(current_max)
