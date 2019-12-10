import sys

value1 = sys.argv[1]

# write your solution here
values = list(value1.split(','))
val = []
val2 = ""

for i in values:
    val.append(int(i))    

val.sort(reverse=True)
for i in val:
    val2 += ''.join(str(i)+',')

print( val2[0:len(val2)-1] )