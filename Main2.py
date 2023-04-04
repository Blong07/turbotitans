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

number_of_cars = 7

# Load images to use for the turtles
# define the car image filenames
Cars = ["PorCh2.gif", "bmCRw2.gif", "ferrar1.gif", "lambo.gif"]
# adds car numbers and loops over car numbers
for i in range (0, number_of_cars - len(Cars)):
    Cars.append(Cars[i])


# create a list of turtle images by adding the car images to the shape dictionary
images = []
for car in Cars:
    turtle.addshape(car)
    images.append(car)

# create six turtles with random images from the list
turtles = []
for i in range(0, number_of_cars):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(-250, -100 + 50 * i)
    t.shape(images[i])
    t.showturtle()
    turtles.append(t)


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
    message = "You have chosen the car, " + str(carnumberX)

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
    message = "You have chosen an unacceptable car fool, " + str(carnumberX)

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


def carnumber():
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
        bad_car(carnumberString)


carnumber()


def racing_turtle(t, distance):
    t.setx(t.xcor() + distance)

print("press space bar to roll dice")

def roll_dice():
    # Roll the dice and move the corresponding turtle
    number = random.randint(1, 6)

    print("Dice rolled: ", number)

    # Move the corresponding turtle
    t = turtles[number - 1]
    racing_turtle(t, 50)


# Bind the roll_dice function to a key press event
window.onkeypress(roll_dice, "space")

# Start the main event loop
window.listen()
turtle.mainloop()

turtle.done()  # Keep the window open until the user closes it
