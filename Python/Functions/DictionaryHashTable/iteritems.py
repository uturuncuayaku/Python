#   Andres Trujillo
#   Python3

from itertools import product

# print (list(product([1,2,3], repeat = 2)))
#[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]

print (list(product([1,2,3])))
# [(1,), (2,), (3,)]

#print (list(product([1,2,3], repeat = 3)))
#[(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 2, 1), (1, 2, 2), 
# (1, 2, 3), (1, 3, 1),
#(1, 3, 2), (1, 3, 3), (2, 1, 1), (2, 1, 2), 
# (2, 1, 3), (2, 2, 1), (2, 2, 2), (2, 2, 3), (2, 3, 1), (2, 3, 2), 
#(2, 3, 3), (3, 1, 1), (3, 1, 2), (3, 1, 3), 
# (3, 2, 1), (3, 2, 2), (3, 2, 3), (3, 3, 1), (3, 3, 2), (3, 3, 3)]

# print (list(product([1,2,3],[3,4])))
#[(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]