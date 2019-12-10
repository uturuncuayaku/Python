# Andres Trujillo
# 11/28/2019
# Python program to convert string to binary

import sys

value1 = sys.argv[1]

print(''.join(format(ord(x),'b')for x in value1))
print(type(''.join(format(ord(x),'b')for x in value1)))
print()

bb = ''.join(map(bin,bytearray(value1,'utf8')))
bbb = bb.split('b')

str1 = ''
print(str1.join(bbb))