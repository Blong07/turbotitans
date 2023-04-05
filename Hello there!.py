import turtle

t = turtle.Turtle()
wn = turtle.Screen()

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    t.write(numbers, align="center", font=("Cooper Black", 25, "italic"))

wn.mainloop()


