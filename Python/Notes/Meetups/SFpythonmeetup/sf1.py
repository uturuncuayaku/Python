#nested data structures
from __future__ import division, print_function
from pprint import pprint

#dictionary
keys = 'guido sarah barry rachel time'.split()
values1 = 'blue orange green yellow red'.split()
values2 = 'austin dallas tuyscon reno portland'.split()
values3 = 'apple banana orange pear peach'.split()

hashes = list(map(abs, map(hash,keys)))
entries = list(zip(hashes,keys,values1))
comb_entries = list(zip(hashes,keys,values1,values2,values3))

def database_linear_search():
    pprint(list(zip(keys,values1,values2,values3)))
