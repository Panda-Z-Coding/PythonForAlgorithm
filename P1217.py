Prime_Palindromes = [5,7,11,101,131,151,181,191,313,353,373,383,727,757,787,797,919,929]
#Prime_Palindromes4 = list()  偶数为都可以写成11的倍数（好像）



def is_Prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True

            
#5位数
for d1 in range(1,10,2):
    for d2 in range(0,10,1):
        for d3 in range(0,10,1):
            palindrome = 10000*d1 + 1000*d2 +100*d3 + 10*d2 + d1
            if is_Prime(palindrome):
                Prime_Palindromes.append(palindrome)

#7位数
for d1 in range(1,10,2):
    for d2 in range(0,10,1):
        for d3 in range(0,10,1):
            for d4 in range(0,10,1):
                palindrome = 1000000*d1 + 100000*d2 +10000*d3 + 1000*d4 + 100*d3 + 10*d2 + d1
                if is_Prime(palindrome):
                    Prime_Palindromes.append(palindrome)


a, b = input().split()

for i in Prime_Palindromes:
    if int(a) <= i <= int(b):
        print(i)

#! AC