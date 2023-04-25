import turtle
from easygui import *
import tkinter as tk

# Create a turtle window
window = turtle.Screen()
window.title("Turbo Titans!")  # sets title of window name

# Set the desired window size
window_width = 1000
window_height = 500

# Set up the window with desired size
window.setup(width=window_width, height=window_height)

# Get the screen width and height
screen_width = window.window_width()
screen_height = window.window_height()

# Get the screen coordinates
screen = turtle.Screen()
root = screen.getcanvas().winfo_toplevel()

# Calculate the window coordinates to center it on the screen
window_x = root.winfo_screenwidth() // 2 - screen_width // 2
window_y = root.winfo_screenheight() // 2 - screen_height // 2

# Set the window position on the screen
root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.bgpic('6track.gif')  # set background image
window.tracer(0)  # turn off screen updates for faster animation
window.update()

# changing the number of cars in the game
# this is set by the amount of cars chosen in the first text box

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
    t.goto(-250, -200 + 50 * i)
    t.shape(images[i])
    t.showturtle()
    t.color("orange") # Set turtle's color to orange
    t.write(i+1, align="left", font=("Cooper Black", 25, "bold")) # Set font to bold





# defining name of user
def chosen_name(name):
    # message / information to be displayed on the screen
    message = "Welcome to the game, " + name

    # title of the window
    title = "Turbo Titans"

    # text of the Ok button
    ok_btn_txt = "Continue"

    # creating a message box
    output = msgbox(message, title, ok_btn_txt)

    # printing the output
    print("User pressed  : " + output)


def chosen_car(carnumberX):
    # message / information to be displayed on the screen
    message = "Well done! You have chosen the car: " + str(carnumberX), "Make sure to press the space bar to move the cars along the track"


    # title of the window
    title = "Turbo Titans"

    # text of the Ok button
    ok_btn_txt = "Continue"

    # creating a message box
    output = msgbox(message, title, ok_btn_txt)

    # printing the output
    print("User pressed  : " + output)


def bad_car(carnumberX):
    # message / information to be displayed on the screen
    message = "You fool, you have chosen the car number:" + str(carnumberX)

    # title of the window
    title = "Turbo Titans"

    # text of the Ok button
    ok_btn_txt = "Continue"

    # creating a message box
    output = msgbox(message, title, ok_btn_txt)

    # printing the output
    print("User pressed  : " + output)

    carnumber()


# asks for name
def hello():
    name = str(turtle.textinput("What is your name?", "Enter your Name"))
    print("hello " + str(name))
    chosen_name(name)
    return


hello()


"""def carnumber():
    carnumberString = turtle.textinput("Enter car between 1 and " + str(number_of_cars), "Enter Car Number")

    try:

        carnumberX = int(carnumberString)

        # print(str(carnumberX) + " is a good car")

        # car selection (choose between 1 - number of cars)
        if carnumberX >= 1 and carnumberX <= number_of_cars:
            chosen_car(carnumberX)
        else:
            # print('you are annoying and stupid')
            bad_car(carnumberX)

            # show a message box that says you have the wrong car
    except:
        bad_car(carnumberString)"""

def carnumber():
    carnumberString = turtle.textinput("Enter car between 1 and " + str(number_of_cars), "Enter Car Number")

    try:
        carnumberX = int(carnumberString)

        if carnumberX >= 1 and carnumberX <= number_of_cars:
            chosen_car(carnumberX)
        else:
            bad_car(carnumberX)
    except ValueError:
        bad_car(carnumberString)



carnumber()


def racing_turtle(t, distance):
    t.setx(t.xcor() + distance)

print("press space bar to roll dice")

def roll_dice():
    # Roll the dice and move the corresponding turtle
    number = random.randint(1, number_of_cars)

    print("Dice rolled: ", number)

    # Move the corresponding turtle
    t = turtles[number - 1]
    racing_turtle(t, 50)

    # Check if the turtle has reached or exceeded the x-coordinate of 250
    if t.xcor() >= 0:
        winner = car_numbers[t]
        msgbox(str(winner) + " wins!", "Winner!")
        #window.bye()  # Close the window and end the game

    # Check for other turtles that have reached or exceeded winning point on X axis
    for t in turtles:
        if t.xcor() >= 0:
            winner = car_numbers[t]
            msgbox(str(winner) + " wins!", "Winner!")




# Bind the roll_dice function to a key press event
window.onkeypress(roll_dice, "space")

import turtle
import random
from easygui import *

# Create a Turtle window
window = turtle.Screen()
window.title("Turbo Titans!")
window.setup(width=500, height=500)

# ... rest of the code ...

# Create a dictionary to store car distances
car_distances = {}
for i in range(1, number_of_cars + 1):
    car_distances[i] = 0

# Function to display winner popup
def display_winner(car_number):
    # Message to be displayed on the screen
    message = str(car_number) + " wins!"

    # Title of the window
    title = "Turbo Titans"

    # Text of the Ok button
    ok_btn_txt = "Continue"

    # Creating a message box
    output = msgbox(message, title, ok_btn_txt)

    # Printing the output
    print("User pressed: " + output)









# Bind the roll_dice function to a key press event
window.onkeypress(roll_dice, "space")

# Start the main event loop
window.listen()
turtle.mainloop()

turtle.done()  # Keep the window open until the user closes it


