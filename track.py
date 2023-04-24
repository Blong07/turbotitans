import turtle
import random

# Create turtle screen
screen = turtle.Screen()

# Set up background image for the screen
screen.bgpic("racingtrackrs.gif")

# Create turtles
number_of_cars = 4  # Change the number of turtles here
turtles = []
colors = ["red", "green", "blue", "orange"]
for i in range(number_of_cars):
    t = turtle.Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(-200, 40 * i - 60)
    t.pendown()
    turtles.append(t)

# Function to move a turtle
def racing_turtle(t, distance):
    t.forward(distance)

# Function to roll dice
def roll_dice():
    # Roll the dice and move the corresponding turtle
    number = random.randint(1, number_of_cars)

    print("Dice rolled: ", number)

    # Move the corresponding turtle
    t = turtles[number - 1]
    racing_turtle(t, 50)

    # Check if turtle has moved 5 spaces
    if t.xcor() >= 5 * 50:
        print(t.color()[0], "turtle has won!")
        return True
    else:
        return False

# Main game loop
while True:
    if roll_dice():
        turtle.done()
        break

    # Check if any turtle has reached the finish line
    for t in turtles:
        if t.xcor() >= 5 * 50:
            print(t.color()[0], "turtle has won!")
            turtle.done()
            break

# Close turtle screen
screen.mainloop()
