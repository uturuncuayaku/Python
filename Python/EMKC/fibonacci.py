# Andres Trujillo
# Python 3
# Recursive slowest way to solve
# Fibonnaci sequence
import sys
from math import *
value1 = sys.argv[1]
value2 = sys.argv[2]

int1, int2 = int(value1),int(value2)
list1 = []
def fibSeq(num, first, sec):
    # print("{},{}".format(first,sec),end="")
    counter = 0
    while(counter < num):
        sum = (first) + (sec)
        # print("{},".format(sec), end="")
        list1.append(sec)

        first = sec
        sec = sum
        counter = counter + 1

def nextFibonacci(x): 
    a = x*(1 + sqrt(5))/2.0
    return round(a) 

n = int2

first = int1
sec = nextFibonacci(int1)

fibSeq(n,first,sec)
val2=''
for i in list1:
    val2 += ''.join(str(i)+',')
print(val2[0:len(val2)-1])
