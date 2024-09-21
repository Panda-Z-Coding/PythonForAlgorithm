a = input()
x = int(a)

def is_even(x):
    if(x % 2 == 0):
        return True
    else:
        return False

def is_Between_4_12(x):
    if(4 < x <= 12):
        return True
    else:
        return False

def A(x):
    if(is_even(x) and is_Between_4_12(x)):
        return 1
    else:
        return 0

def Uim(x):
    if(is_even(x) or is_Between_4_12(x)):
        return 1
    else:
        return 0
    
def B(x):
    if((is_even(x) == True and is_Between_4_12(x) == False) or (is_even(x) == False and is_Between_4_12(x) == True)):
        return 1
    else:
        return 0
    
def zhen(x):
    if(is_even(x) == False and is_Between_4_12(x) == False):
        return 1
    else:
        return 0
    
print(A(x),end=' ')
print(Uim(x),end=' ')
print(B(x),end=' ')
print(zhen(x),end='')