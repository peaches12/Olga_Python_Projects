#the program will create a function to draw a square

def draw_square(side):
    
    wn=turtle.Screen()
    pen=turtle.Turtle()
    for i in range(4):
        pen.forward(side)
        pen.left(90)
    return(pen)


    
