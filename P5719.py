import sys
n,k = sys.stdin.readline().split()
class_num1 = list()
class_num2 = list()
for nn in range(1,int(n) + 1):
    if(int(nn) % int(k) == 0):
        class_num1.append(nn)
    else:
        class_num2.append(nn)

avr1 = sum(class_num1) / len(class_num1)
avr2 = sum(class_num2) / len(class_num2)

print("{:.1f}".format(avr1),end = ' ')
print("{:.1f}".format(avr2),end = '')
