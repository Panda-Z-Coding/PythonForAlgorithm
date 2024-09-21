'''
全部吃完的总时间是m*t,时间过了s分钟,所以吃完剩下的苹果时间是m*t-s,那么剩下的苹果是m*t-s//t个
'''

m, t, s = input().split()
if(int(t) > 0):
    a = (int(m)*int(t)-int(s))//int(t)
elif(int(t) == 0):
    a = 0

if(a > 0):
    print(a)
elif(a == 0):
    print(a)
else:
    print(0)