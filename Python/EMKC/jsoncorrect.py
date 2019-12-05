import sys

value1 = sys.argv[1]

# JSON needs beginning and ending curly braces
# Json needs beginning and ending quotation marks around variable name and value
# missing comma between properties

listString = list(value1)

listsz = len(listString)

didPassed1 = False;


    for i in range(0, listsz, 1):
        while(listString[i] == '{' ):
            for j in range(0, listsz, 1):
                j = j + j
                if(listString[j] == '}' ):
                    didPassed1 = True
                else:
                    didPassed1 = False
                    break    



print(list(value1)) # debug line

list(value1)