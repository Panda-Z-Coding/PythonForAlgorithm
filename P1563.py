'''P1563 [NOIP2016 提高组] 玩具谜题'''

def outOrIn(direction: int,head: int) -> bool:
    # 总合向左就返回True
    if direction == 0 and head == 0:
        return True
    elif direction == 0 and head == 1:
        return False
    elif direction == 1 and head == 0:
        return False
    elif direction == 1 and head == 1:
        return True 

# n行m列
n ,m = input().split()
n = int(n)
m = int(m)
set = 0 # 要走的步长和方向
people = {} # 空字典
persons = list() # 存人物圈
for i in range(n):
    d, job = input().split()
    people[job] = int(d)
    persons.append(job)
# 创建字典，名字对应0或1
for i in range(m):
    head, nums = input().split()
    if outOrIn(people[persons[(set + len(persons)) % len(persons)]],int(head)):
        set -= int(nums)
    else:
        set += int(nums)

print(persons[(set + len(persons)) % len(persons)])
        
# AC!
