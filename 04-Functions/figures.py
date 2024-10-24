import turtle
def draw_square(lengtha, lenghtb):
    # Create the turtle
    pen = turtle.Turtle()
    pen.speed(5)

    for i in range(3):
        pen.forward(lengtha)
        pen.right(120)
    pen.penup()
    pen.goto(-75, 75)
    pen.pendown()
    for i in range(3):
        pen.forward(lengtha)
        pen.right(120)
    pen.penup()
    pen.goto(-250, 250)
    pen.pendown()
    for i in range(2):
        pen.forward(lengtha)
        pen.right(90)
        pen.forward(lenghtb)
        pen.right(90)
    
    pen.hideturtle()