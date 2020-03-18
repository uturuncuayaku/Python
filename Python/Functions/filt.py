"""
*************************
*   Andres Trujillo    *
*   12/7/2019           *
*************************   

Python3

filter() method

    Definition:
        
        Filters the given sequence with the help of a
        function that that tests each element in the
        sequence to be true or not.

"""
def functionthatfiltersvowels(stringtobechecked):
    letters = ['a','e','i','o','u']
    if(variable in letters):
        return True
    else:
        return False
sequence=[ "How many vowels are in this sentence?" ]
filtered= filter(functionthatfiltersvowels,sequence)

print('The filtered letters are:')
for s in filtered:
    print(s)


seq = [0,1,2,3,4,5,6,7,8,9,10]
result = filter(lambda x: x%2,seq)
print(list(result))

result = filter(lambda x:x%2==0, seq)
print(list(result))

    




