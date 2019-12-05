#   Andres Trujillo
#   Python Implementation of Introsort Algorithm
#   November 19, 2019

import math
import sys
from heapq import heappush, heappop

arr =[]

def heapsort():
    global arr
    h=[]

    #heap

for value in arr:
    heappush(h,value)
    arr=[]

    #extract
    arr = arr+[ heappop(h) for i in range(len(h)) ]

    #sort
    def InsertionSort(begin, end)
    left =begin
    right =end

    #traverse
    for i in range(left+1,right+1):
        key =arr[i]

        #move elements of array that are
        #greater than the key to one position
        #ahead of current position

        j=i-1
        while j>= left and arr[j]
            arr[j+1] = arr[j]
            j=j-1
        arr[j+1] = key

    #function taking last element as pivot
    #places pivot element at correct
    #position in sorted array
    #places all smaller than pivot
    #to left of pivot variable
    #all greater elements to right of pivot

    def Partition(low,high):
        global arr

    #pivot
        pivot =arr[high]

    #index of small element
        i =low-1

    for j in range(low,high):

        #if current element is smaller/equal
        #to the pivot

        if arr[j] <= pivot:
            #increment index of smaller element

            i=i+1
            (arr[i], arr[j])= (arr[j],arr[i])
            (arr[i+1], arr[high])= (arr[high], arr[i+1])
        return i+1

    

        










        
