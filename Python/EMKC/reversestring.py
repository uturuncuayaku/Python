# Andres Trujillo
# Easy Python

import sys

# Argument string array
value1 = sys.argv[1]

wordLength = len(value1)
reversed_word = ''

for count in range(0-1, -(wordLength+1), -1):
    reversed_word = reversed_word + value1[count]

print(reversed_word)
        
