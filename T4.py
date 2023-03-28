"""import turtle
turtle.showturtle()
turtle.shape("turtle")
turtle.shape("turtle")

# load the appropriate image
turtle.bgpic()
turtle.penup()
# bring the turtle to the starting point
turtle.goto(-70, 210)"""

import turtle
dum = turtle.Turtle
dee = turtle.Turtle
doo = turtle.Turtle

window = turtle.Screen()
window.addshape("porch1.gif")
turtle.shape("porch1.gif")
turtle.showturtle()

"""
#dum = turtle
dum = turtle.Turtle()
window = dum.Screen()
window.addshape("porch1.gif")
dum.shape("porch1gif")
dum.showdum()


dee = turtle.Turtle()
doo = turtle.Turtle()
"""
"""import turtle

# Create a Turtle window
window = turtle.Screen()

# Load a custom image for the turtle
window.addshape("porch1.gif")"""

# Create a Turtle object
# t = turtle.Turtle()

# Set the shape of the turtle to the custom image
#t.shape("porch1.gif")

# Resize the turtle
turtle.shapesize(stretch_wid=1, stretch_len=1)

# Keep the window open until the user closes it
#turtle.done()

window.bgpic('racetrack.gif') # image should be PNG or GIF
window.update() # to show the imagemainloop()

#dee.goto(-50, 210)
turtle.goto(-70, 210)
turtle.left(90)
turtle.forward(100)