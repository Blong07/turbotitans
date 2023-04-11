import turtle
import random
from easygui import *

# Create a Turtle window
window = turtle.Screen()
window.title("Turbo Titans!")
window.setup(width=500, height=500)

# Load background image for the turtle window
window.bgpic('6track.gif')
window.setup(width=2000, height=2000)
window.update()

# Define the number of cars in the game
number_of_cars = 10

# Define the car image filenames
Cars = ["PorCh2.gif", "bmCRw2.gif", "ferrar1.gif", "lambo.gif"]

# Duplicate the car images if there are fewer than number_of_cars
for i in range(len(Cars), number_of_cars):
    Cars.append(Cars[i % len(Cars)])

# Create a list of turtle images by adding the car images to the shape dictionary
images = []
for car in Cars:
    turtle.addshape(car)
    images.append(car)

# Write a number on the turtle image ranging from 1 - x
def car_number(num):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(-20, -10)
    t.write(num, font=("Arial", 10, "normal"))

# Create turtles with random images from the list
turtles = []
for i in range(number_of_cars):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(-250, -100 + 50 * i)
    t.shape(images[i])
    car_number(i + 1)
    t.showturtle()
    turtles.append(t)

# Ask for the user's name
def get_name():
    name = turtle.textinput("What is your name?", "Enter your Name")
    print("Hello " + name)
    chosen_name(name)

# Define what happens when the user enters their name
def chosen_name(name):
    message = "Welcome to the game, " + name
    title = "Turbo Titans"
    ok_btn_txt = "Continue"
    output = msgbox(message, title, ok_btn_txt)
    print("User pressed: " + output)

# Ask for the user's chosen car number
def get_car_number():
    car_number_string = turtle.numinput("Enter car between 1 and " + str(number_of_cars), "Enter Car Number", minval=1, maxval=number_of_cars)

    if car_number_string is not None:
        car_number = int(car_number_string)
        chosen_car(car_number)
    else:
        bad_car()

# Define what happens when the user enters a valid car number
def chosen_car(car_number):
    message = "You have chosen car " + str(car_number)
    title = "Turbo Titans"
    ok_btn_txt = "Continue"
    output = msgbox(message, title, ok_btn_txt)
    print("User pressed: " + output)

    # Bind the roll_dice function to a key press event
    window.onkeypress(roll_dice, "space")

# Define what happens when the user enters an invalid car number
def bad_car():
    message = "You have not chosen a valid car number."
    title = "Turbo Titans"
    ok_btn_txt = "Continue"
    output = msgbox(message, title, ok_btn_txt)
    print("User pressed: " + output)
    get_car_number()

# Start the game by getting the user's name and chosen car number
get_name()
get_car_number()

# Define the function to move a turtle a given distance
# Define the function to roll the dice and move the corresponding turtle

turtle.done()  # Keep the window open until the user closes it

def racing_turtle(t, distance):
    x, y = t.position()
    t.goto(x + distance, y)

