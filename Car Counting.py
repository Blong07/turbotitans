images = []
for car in Cars:
    turtle.addshape(car)
    images.append(car)

def car_number(num):
    turtle.write(num, align="center", font=("Cooper Black", 25, "italic"))

# create six turtles with random images from the list
turtles = []
for i in range(0, number_of_cars):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(-250, -100 + 50 * i)
    t.shape(images[i])
    car_number(i + 1)
    t.showturtle()
    turtles.append(t)
