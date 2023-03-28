import turtle

# Create a Turtle window
window = turtle.Screen()
window.title("Turbo Titans!") # sets title of window name
window.setup(width=500,height=500)

# Load images to use for the turtles
turtle.addshape("PorCh2.gif")
turtle.addshape("bmCRw2.gif")
turtle.addshape("ferrar1.gif")
turtle.addshape("lambo.gif")

# ("bmw1.gif").setup(width=50,height=50) # this code was abysmal and does not work at all

# setup(width=50,height=50)

# turtle.addshape("Porch1.gif") # only need to specify what turtle shape is once, unless using multiple shapes

#Turtle Loading...

t1 = turtle.Turtle()
t1.shape("PorCh2.gif")
#t1.color("cyan")

"""def increaseSize():
    size = t1.turtlesize()
    increase.size = tuple([2 * num for num in size])
    t1.turtlesize(incr) #this is where the error occurs

ws.onkey(increaseSize "2")
wslisten()
turtle.done()"""

# t1.resizemode("auto")

t2 = turtle.Turtle()
t2.shape("bmCRw2.gif")

t3 = turtle.Turtle()
t3.shape("ferrar1.gif")
"""t3.penup()"""

t4 = turtle.Turtle()
t4.shape("lambo.gif")
t4.hideturtle()
t4.penup()
t4.goto(-30,210)
t4.showturtle()



window.bgpic('6track.gif')#had to be gif to work
window.setup(width=2000,height=2000)
window.update()

"""t1.shapesize(stretch_wid=2, stretch_len=2)
t2.shapesize(stretch_wid=0.5, stretch_len=0.5)"""


#I thought each 'turtle' needed a screen, however there is only one 'window' needed for all turtles.
#window = t1.Screen()
"""window.addshape("Porch1.gif")
t1.shape("Porch1.gif")"""







# t2
t2.hideturtle()
t2.penup()
t2.goto(-70, 80)
t2.showturtle()

# t1
t1.hideturtle()
t1.penup()
t1.goto(-70, 210)
t1.showturtle()
t1.right(300)
t1.forward(200)

#input("What is your name?")
#print


#asks for name
def hello():
    name=str(input("What is your name? : "))
    print("hello " + str(name))
    return
hello()


def carnumber():
    print("Choose a car between 1 and 6")
    carnumberX= int(input("enter car number : "))

    print(str(carnumberX) + " is a good car")

    while True:
        #age = input('Are you 1,2 OR 3')
        if carnumberX >= 1 and carnumberX <=6:
            break
        else:
            print('you are annoying and stupid')


carnumber()





#playing rounds
"""def play_roundx():
    roll = random.randint(1,6)
    print("the dice rolled:", roll)"""






turtle.done() # Keep the window open until the user closes it
