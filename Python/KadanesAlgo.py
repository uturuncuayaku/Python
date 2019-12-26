# Kadanes Algorithm
#   Usage: Find the maximum sub of two numbers in an array.
#   Work: O(n)

#Setting two variables called max_current and max_global
#to the first index'd number in Array 'A'

#Slicing array excluding the first element
#from loop to the last element 'A[1:]'

#max(a,b) function takes two numbers and returns the larger number
#Saving the maximum number from the current global or the current number
#added to the next number in array as 'x'

#Taking note that max_current and max_global at first iteration is
#the same value.

#If the max of the next 'x' is greater than the first index'd global
#added to the first element in array we save it as max_current


def maximum_in_subarray(A):
    max_current = max_global = A[0]
    for x in A[1:]:
        max_current = max(x, max_current + x)
        max_global = max(max_global, max_current)
    return max_global

def max_in_subarray(B):
    max_curr = max_global1 = B[0]
    for y in B[1:]:
        max_curr = max(y, max_curr + x)
        if (max_curr > max_global1):
            max_global1 = max_curr
    return max_global1
