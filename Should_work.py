import turtle
import random

# set up the TurtleScreen
window = turtle.Screen()
window.bgpic('6track.gif')
window.setup(width=2000, height=2000)
window.update()

# define the car image filenames
Cars = ["PorCh2.gif", "bmCRw2.gif", "ferrar1.gif", "lambo.gif"]

# create a list of turtle images by adding the car images to the shape dictionary
images = []
for car in Cars:
    turtle.addshape(car)
    images.append(car)

# create six turtles with random images from the list
turtles = []
for i in range(1, 7):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(-250, -100 + 50 * i)
    t.shape(random.choice(images))
    t.showturtle()
    turtles.append(t)

# start the turtle event loop
turtle.mainloop()

