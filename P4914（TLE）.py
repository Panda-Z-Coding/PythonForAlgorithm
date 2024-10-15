'''
选定x,y为中心的2r+1的矩阵进行0(顺时针),1(逆时针)

    那么(x-r),(y-r)就是要转换的矩阵的左上角起始位置,循环2r+1次,放入新的矩阵的for j for i -> (x-r+i),(y+r-j)

'''

def rotate(x,y,r,z):
    l = 2*r + 1
    li = [row[y-r-1:y+r] for row in matrix[x-1-r:x+r]]
    if z == 0:
        # for i in range(l):
        #     li.append(matrix[x-r+i-1][y-r-1:y-r+l-1])
        for z in range(l):
            for j in range(l):
                matrix[x-r+j-1][y+r-z-1] = li[z][j]
        # li.clear()    
        
            
    else:
        # for i in range(l):
        #     li.append(matrix[x-r+i-1][y-r-1:y-r+l-1])
        for z in range(l):
            for j in range(l):    
                matrix[x+r-j-1][y-r+z-1] = li[z][j]
        # li.clear()
        
    return
    


n, m = map(int, input().split())
matrix = [[i * n + j + 1 for j in range(n)] for i in range(n)]

#翻转
for i in range(m):
    x, y, r, z = map(int,input().split())
    rotate(x,y,r,z)  
    
for row in matrix:
    print(' '.join(map(str, row)))

# 60 ; 超时了T_T,Python还是太慢了