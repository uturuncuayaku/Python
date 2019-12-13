def spiral(step, angle, max):                                                                                           
    for i in range(0, max, step):                                                                                       
        turtle.forward(i*3)                                                                                             
        turtle.left(126.87)                                                                                             
        turtle.forward(i*5)                                                                                             
        turtle.left(143.2)                                                                                              
        turtle.forward(i*4)                                                                                             
        turtle.left(90 + angle)