import heapq
n, m = input().split()

ballot = list(map(int, input().split()))

#! 插入排序太慢了，TLE
# def selec_sort(l):
#     for i in range(len(l)):
#         for j in range(i+1,len(l)):
#             if l[j] < l[i]:
#                 l[i], l[j] = l[j], l[i]
#     return l

# ans = selec_sort(ballot)
ballot.sort()
    


                
print(" ".join(map(str,ballot)))                
