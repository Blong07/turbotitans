import turtle
import random

# Create a turtle window
wn = turtle.Screen()
wn.title("Dice Roll Turtle Game")
wn.setup(width=600, height=400)

# Create 6 turtles for each dice number
turtles = []
for i in range(1, 7):
    t = turtle.Turtle(shape="turtle")
    t.penup()
    t.goto(-250, -100 + 50 * i)
    turtles.append(t)


# Function to move a turtle along the x axis
def move_turtle(t, distance):
    t.setx(t.xcor() + distance)


# Function to roll a dice and move the corresponding turtle
def roll_dice():
    # Roll the dice and move the corresponding turtle
    number = random.randint(1, 6)
    print("Dice rolled: ", number)

    # Move the corresponding turtle
    t = turtles[number - 1]
    move_turtle(t, 50)


# Bind the roll_dice function to a key press event
wn.onkeypress(roll_dice, "space")

# Start the main event loop
wn.listen()
turtle.mainloop()
