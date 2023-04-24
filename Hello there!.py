import turtle
import random
from easygui import *

# Create a Turtle window
window = turtle.Screen()
window.title("Turbo Titans!")  # sets title of window name
window.setup(width=500, height=500)

window.bgpic('6track.gif')#had to be gif to work
window.setup(width=2000,height=2000)
window.update()

# changing the number of cars in the game
# # # Modify number_of_cars using easygui
number_of_cars = enterbox("Enter number of cars", "Menu", default="10")
number_of_cars = int(number_of_cars)

# Load images to use for the turtles
# define the car image filenames
Cars = ["PorCh2.gif", "bmCRw2.gif", "ferrar1.gif", "lambo.gif"]

# adds car numbers and loops over car numbers
for i in range (0, number_of_cars - len(Cars)):
    Cars.append(Cars[i])


# create a list of turtle images by adding the car images to the shape dictionary
images = []
turtles = []  # Move turtles list creation here
for car in Cars:
    turtle.addshape(car)
    images.append(car)
    turtles.append(turtle.Turtle())  # Append a new turtle to the turtles list


# create a dictionary to store car numbers
car_numbers = {}
for i in range(1, number_of_cars + 1):
    car_numbers[turtles[i - 1]] = i


# create six turtles with random images from the list
for i in range(0, number_of_cars):
    t = turtles[i]  # Use the existing turtle from the turtles list
    t.hideturtle()
    t.penup()
    t.goto(-250, -100 + 50 * i)
    t.shape(images[i])
    t.showturtle()
    t.color("orange") # Set turtle's color to orange
    t.write(i+1, align="left", font=("Cooper Black", 25, "bold")) # Set font to bold


def chosen_car(car_num):
    # Loop through all the turtles to update the color of the chosen car number to orange
    for t in turtles:
        t.color("orange") # Set turtle's color to orange
        if car_numbers[t] == car_num:
            t.color("black") # Set turtle's color back to black for the chosen car number
            t.write(car_num, align="left", font=("Cooper Black", 25, "bold")) # Write the car number to the left of the turtle


# Function to move the turtles
def move_cars():
    for t in turtles:
        t.forward(random.randint(5, 25))
        if t.xcor() > 230:  # check if turtle crosses the finish line
            winner = car_numbers[t]
            print("Car number", winner, "wins!")
            chosen_car(winner)
            return winner
    return None


# Main game loop
while True:
    # Update window and check for collisions
    window.update()

    # Move the cars
    winner = move_cars()

    # Check for winner
    if winner is not None:
        turtle.done()
        break

turtle.done()





