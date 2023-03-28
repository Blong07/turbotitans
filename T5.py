import turtle
window = turtle.Screen()
window.addshape("porch1.gif")
turtle.shape("porch1.gif")


# open the image file
image = turtle.open("Porch1.gif")

# set the size of the new image
new_size = (80, 60)

# resize the image
resized_image = image.resize(new_size)

# save the resized image to a new file
resized_image.save("Porch1.gif")

window.bgpic('racetrack.gif') # image should be PNG or GIF
window.update() # to show the imagemainloop()

turtle.goto(-70, 210)

