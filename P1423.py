s = float(input())
swim_len = 2.0
sum_len = 0.0
ans = 0

while sum_len < s:
    sum_len += swim_len
    swim_len *= 0.98
    ans += 1

print(ans)
