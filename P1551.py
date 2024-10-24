"""
并查集模板题 -> P1551 亲戚

"""
# 初始化并查集，让每个父亲节点都为他自己
def init_Dsu(n):
    return [i for i in range(n+1)]


def find(x):
    if x == Dsu[x]:
        return x
    else:
        Dsu[x] = find(Dsu[x]) #路径压缩
        return Dsu[x] #返回父亲节点

def uinonn(i, j): # 把i和j合并
    i_fa = find(i)
    j_fa = find(j)
    Dsu[i_fa] = j_fa #把i祖先换成j的祖先
    
n, m, p = map(int, input().split())
# 初始化并查集，让每个父亲节点都为他自己
# Dsu = [i for i in range(n+1)]
Dsu = init_Dsu(n) #n个亲戚
# print(Dsu)

for _ in range(m):
    i, j = map(int, input().split())
    uinonn(i, j)

for _ in range(p):
    i, j = map(int, input().split())
    if find(i) == find(j):
        print("Yes")
    else:
        print("No")