"""
金币
"""

k = int(input())
day = 1
sum_coin = 0
coin = 1

while True:
    if day > k:
        break
    for i in range(1,coin + 1):
        if day > k:
            break
        day += 1
        sum_coin += coin
    coin += 1


print(sum_coin)

#! AC