"""
用一个二维数组来存储（从1开始），
    第0位表示总分，第1位表示语文成绩
    第2位表示学号
"""

#存储原本的成绩
socre = [0] * 3

#存储总分、语文、学号
sum_socre = []

n = int(input())
for i in range(1,n + 1):
    yu, su, yin = map(int, input().split())
    sum_ = yu + su + yin
    sum_socre.append([sum_, yu, i])
#按照总分，语文降序,其他升序
sum_socre.sort(key= lambda x:(x[0],x[1]),reverse= True)
#print(sum_socre)


for i in range(5):
    print(sum_socre[i][2], end=' ')
    print(sum_socre[i][0])
