def is_pronic(x):
    #Happy Coding ^_^
    if (x == 0):
      return True
    for n in range(x):
      if(n *(n+1) == x):
        return True
    return False
