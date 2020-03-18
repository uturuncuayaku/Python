"""
8 kyu
guessBlue() -  probability of drawing a blue marble

* blue_start: the number of blue marbles you put in the bag to start
* red_start: the number of red marbles you put in the bag to start
* blue_pulled: the number of blue marbles pulled out so far 
* 	(always lower than the starting number of blue marbles)
* red_pulled: the number of red marbles pulled out so far 
* 	(always lower than the starting number of red marbles)

For example, guessBlue(5, 5, 2, 3) should return 0.6.

"""
def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    
    #Started off on the wrong foot
    #with the total marble amount
    #but figured out the opposite of the total
    #is the amount of marbles left
    #and computes a proper combinational
    #probabilistic outcome
    #total = blue_start + red_start
    
    blue = blue_start - blue_pulled
    red  = red_start  - red_pulled
    
    # blue marbles left is divided
    # by the total amount of marbles left
    # in this case only red marbles are left
    return blue/(blue + red)
    
    
