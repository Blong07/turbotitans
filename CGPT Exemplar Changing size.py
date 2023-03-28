"""import turtle

# Create a Turtle window
window = turtle.Screen()

# Load images to use for the turtles
turtle.addshape("Porch1.gif")
turtle.addshape("bmw1.gif")

# Create two turtles with different shapes
t1 = turtle.Turtle()
t1.shape("bmw1.gif")
t1.shapesize(stretch_wid=0.5, stretch_len=0.5)

t2 = turtle.Turtle()
t2.shape("Porch1.gif")
t2.shapesize(stretch_wid=1.5, stretch_len=1.5)

# Move the turtles to different positions
t1.penup()
t1.goto(-100, 0)
t1.pendown()

t2.penup()
t2.goto(100, 0)
t2.pendown()

# Make the turtles move
t1.forward(50)
t2.backward(50)

# Keep the window open until the user closes it
turtle.done()"""


# #ChatGPT said this module is important

from PIL import Image

import turtle


# Create a Turtle window
window = turtle.Screen()

# Open the image file and resize it
#image1 = Image.open("bmw1.gif")
#resized_image1 = image1.resize((100, 100))

#New code, should be defined
Image = ("bmw1.gif")

resized_image1 = Image.resize((100, 100))

# Load the resized image to use as the turtle shape
turtle.addshape("bmw1.gif", shape=resized_image1)

# Create a turtle with the resized shape
t1 = turtle.Turtle()
t1.shape("bmw1_resized.gif")

#load background
window.bgpic('racetrack.gif') # image should be PNG or GIF
window.update()

# Move the turtle and make it move
t1.penup()
t1.goto(-50, 0)
t1.pendown()
t1.forward(50)

# Keep the window open until the user closes it
turtle.done()

