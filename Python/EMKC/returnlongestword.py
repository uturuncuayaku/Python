import sys
import re

value1 = sys.argv[1]

# write your solution here
vals1 = ''
print(value1)
for word in value1:
    vals1 += ''.join(value1.split(','))
print(vals1)

# for word in value1.split(', |):
#     vals1.append(word)

# maxLength = max(len(x) for x in vals1)
    # length = max(map(len,value1))
    # if(length == len(word)):
# newlist = [s for s in vals1 if len(s) == maxLength]

# print(vals1)
