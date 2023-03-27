import turtle
from turtle import Turtle
name=''
img =""
coordinates = (0,0)
mlist = [] #empty currently

#create a func that I can call to add a new bike to the list

def add_new_bike(x,y, img, name):
    # add new object
    name = Turtle()
    name.goto(x,y)
    turtle.addshape("ferrar1.gif")
    name.shape()

    # and object to the list
    mlist.append(name) # append adds to, link in chain

#call the function
add_new_bike(0, 0,'ferrar1.gif', "yamaha")
add_new_bike(10, 10, 'ferrar1.gif', "bmw")

imglist=["ferrar1.gif", "bmCRw2.gif", "PorCh2.gif", "lambo.gif"]
namelist= ["t1", "t2", "t3", "t4"]
for number in range(6): # i is for items
    print (number)
    add_new_bike(x+number, y+number, img[list[number]], namelist[number])


print(mlist)

for item in mlist:
    print(item)



