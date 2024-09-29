
def bigger_Prime(n):
    for i in range(2,int(n**0.5) + 1,1):
        if n % i == 0:
            return n // i
n = int(input())
        
print(bigger_Prime(n))
