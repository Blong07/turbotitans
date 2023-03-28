
"""#import ("lambo.png")

#trying to import lambo png
image = image.open(lambo.png)
import (image)
import random

import turtle
turtle.showturtle('porch-removebg-preview.png')
turtle.shape("turtle")
#loads the turtle shape!!!
turtle.bgpic()
turtle.goto(-70, 210)
turtle.pendown()
turtle.pencolor("red")
turtle.forward(100)

import turtle
window = turtle.Screen()
window.addshape("porch1.gif")
turtle.shape("porch1.gif")




import turtle2
window = turtle2.Screen()
window.addshape("porch1.gif")
turtle2.shape("porch1.gif")




window.bgpic('racetrack.gif') # image should be PNG or GIF
window.update() # to show the imagemainloop()

turtle.goto(-70, 210)
turtle.right(0)
turtle.forward(30)"""


#Break bewteen two codes

# initialize starting positions for each object
positions = [0, 0, 0, 0, 0, 0]

# define function to play one round of the game
def play_round():
    roll = random.randint(1,6)
    print("The dice rolled:", roll)
    for i in range(len(positions)):
        if roll == i+1:
            positions[i] += 1
            print("Object", i+1, "moved forward to position", positions[i])
        else:
            print("Object", i+1, "stays in position", positions[i])

# play game until one object reaches 5
while max(positions) < 5:
    input("Press Enter to roll the dice.")
    play_round()

# declare winner
winner = positions.index(max(positions))+1
print("Object", winner, "wins!")

print("well done", winner, "you are the winner")


