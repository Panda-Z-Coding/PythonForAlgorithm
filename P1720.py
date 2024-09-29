n = int(input())

#print("{:.2f}".format((((1 + 5**0.5) / 2)**n - ((1 - 5**0.5) / 2)**n) / 5**0.5))

def fibonacci(x):
    if x <= 0:
        return 0
    elif x == 1:
        return 1
    
    fib = [0] * (x + 1)
    fib[1] = 1
    
    for i in range(2, x + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[x]

print("{:.2f}".format(fibonacci(n)))
