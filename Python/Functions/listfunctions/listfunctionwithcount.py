"""
#    Andres Trujillo
#    Python 3.8
#    List function | count()
#    12/05/2019
"""

list1 = [1, 1, 1, 2, 3, 2, 1]
print(list1.count(1)) #looking for ones with python count function
#there are 4 ones in list1

list2 = ['a', 'a', 'a', 'b', 'b', 'a', 'c', 'b']
print(list2.count('b')) #looking for the amount of letter b's in list2
#found 3 b's

list3 = ['Cat', 'Bat', 'Sat', 'Cat', 'cat', 'Mat'] 
print(list2.count('Cat'))#find the number of times we find Cat
#we find cat once and only print Cat found twice

#count('oneparameter') is only argument
list122 = [('Cat', 'Bat'), ('Sat', 'Cat'), ('Cat', 'Bat'), \
          ('Cat', 'Bat', 'Sat'), [1, 2], [1, 2, 3], [1, 2] ]
print(list122.count(('Cat','Bat')))#still only one parameter but this time is a paired list in position 1 of list122



#count the number of times and obj appears in a list using count()
#method
lst= ['Cat', 'Bat', 'Sat', 'Cat', 'Mat', 'Cat', 'Sat']

newlist = []
newlist = ([[l, lst.count(l)] for l in set(lst)])
print(newlist)

newlist1 = []
newlist1= (dict((l,lst.count(l)) for l in set(lst)))
print(newlist1)