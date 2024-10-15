    # '''
    # (i + m) % m 循环
    # if len(list) == 0:
    #     break
    # '''

    # n, m = map(int, input().split())
    # arr = [ _ for _ in range(1,n+1)]
    # i = 0
    # ans = []

    # while len(arr):
    #     # p = (i + len(arr) - 1) % len(arr)
    #     v = arr.pop((i + m - 1) % len(arr))
    #     ans.append(v)
    #     i += m - 1
        

    # print(ans)

from collections import deque

def josephus(n, m):
    """
    解决约瑟夫问题，返回出列顺序列表。
    
    参数：
    n -- 总人数
    m -- 报数的上限，报到m的人出列
    
    返回：
    List[int] -- 出列顺序
    """
    # 初始化队列，队列中存储的是人的编号
    queue = deque(range(1, n + 1))
    elimination_order = []
    
    while queue:
        # 报数到m-1的人移动到队列末尾
        for _ in range(m - 1):
            person = queue.popleft()
            queue.append(person)
        
        # 报数到m的人出列
        eliminated = queue.popleft() 
        elimination_order.append(eliminated)
    
    return elimination_order

n, m = map(int, input().split())
ans = josephus(n, m)

print(" ".join(map(str,ans)))
        