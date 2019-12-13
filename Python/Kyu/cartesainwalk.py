def isValidWalk(walk):
    #determine if walk is valid
    print(walk)
    pass
for i in range(2): # test as many times as you want, just change the number
    test1 = create_tests(random.randint(0,20))
    test.assert_equals(isValidWalk(test1[0]),test1[1])
    
    
def isValidWalk1(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')