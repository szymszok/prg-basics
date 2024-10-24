import turtle
from figures import draw_square

# Set up the screen
window = turtle.Screen()
window.bgcolor("grey")

side_lenghta = 200
side_lenghtb = 100
draw_square(side_lenghta, side_lenghtb)


# Finish

window.mainloop()