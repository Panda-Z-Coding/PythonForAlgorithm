import sys

score = list()

def read_until_E():
    while True:
        # 25个字符为一行
        line = input()
        if not line:
            break
        if 'E' in line:
            index_E = line.index('E')
            #切片
            line = line[:index_E + 1]
            score.extend(line)
            break
        else:
            score.extend(line)

def split_11(s):
    count_w = 0
    count_l = 0
    for i in score:
        if i == 'W':
            count_w += 1
        if i == 'L':
            count_l += 1
        if i == 'E':
            print(f"{count_w}:{count_l}")
            print()
            break
        if count_w - count_l >= 2 or count_l - count_w >= 2:
            if count_w >= 11 or count_l >= 11:
                print(f"{count_w}:{count_l}")
                count_w = 0
                count_l = 0

def split_21(s):
    count_w = 0
    count_l = 0
    for i in score:
        if i == 'W':
            count_w += 1
        if i == 'L':
            count_l += 1
        if i == 'E':
            print(f"{count_w}:{count_l}")
            print()
            break
        if count_w - count_l >= 2 or count_l - count_w >= 2:
            if count_w >= 21 or count_l >= 21:
                print(f"{count_w}:{count_l}")
                count_w = 0
                count_l = 0

read_until_E()
split_11(score)
split_21(score)