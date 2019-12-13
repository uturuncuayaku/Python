def descending_order(num):
    # Bust a move right here
    x =[]
    x=list(str(num))
    x.sort(reverse=True)
    z=''
    for i in x:
        z= z+i
    return(int(z))

    # # def Descending_Order(num):
    # return int("".join(sorted(str(num), reverse=True)))