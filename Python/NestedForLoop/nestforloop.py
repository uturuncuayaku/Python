i = 2
while(i < 100):
    j = 2

    while(j <= (i/j)):

        print(str(i/j))
        print("j: "+str(j) +" " + "i: "+str(i))
        print("MOD"+str(i%j))

        if not(i%j): break
        print("MOD"+str(i%j))
        j = j + 1

    if (j > i/j) : 

        print(str(i)+  " is prime")
        
    i = i + 1

