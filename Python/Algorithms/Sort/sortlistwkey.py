#	Andres Trujillo
#	11/26/2019
#	Sort a list using the key

def takeSecond(element):
	return element[1]

random = [(2,2), (3,4), (4,1), (1,3)]

random.sort(key=takeSecond)

print('Sorted list:', random)
