import sys

value1 = sys.argv[1]
num =[]

num = max(set(value1), key = value1.count)
print(num)