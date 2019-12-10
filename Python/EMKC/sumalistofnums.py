import sys

value1 = sys.argv[1]

added1 = []
added = list(value1.split(','))

for i in added:
    added1.append(int(i))

print(sum(added1))
