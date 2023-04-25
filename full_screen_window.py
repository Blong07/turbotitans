import turtle
from AppKit import NSScreen

# Create a turtle window
window = turtle.Screen()

# Get the screen resolution
screen_width = int(NSScreen.mainScreen().frame().size.width)
screen_height = int(NSScreen.mainScreen().frame().size.height)

# Set the window dimensions to match the screen resolution
window.setup(width=screen_width, height=screen_height)

# Rest of your code goes here

# Close the turtle window when done
window.bye()

