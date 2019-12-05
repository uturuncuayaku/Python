import sys

#value1 = sys.argv[1]

# JSON needs beginning and ending curly braces
# Json needs beginning and ending quotation marks around variable name and value
# missing comma between properties

value1 = '"name":"somebody"}'
listString = list(value1)

listsz = len(listString)
didPassed1 = False
fixedString = ""
normalString = ''.join(listString)

if(listString[0] != '{' or listString[-1] != '}'):
    fixedString = '{'
    for i in range(0,listsz):
        fixedString = fixedString + listString[i]
    didPassed1 = True
    fixedString = fixedString + '}'

if not (didPassed1):
    print('Normal: '+normalString)
else:
    print('Fixed'+fixedString)


    



