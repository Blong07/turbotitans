import turtle
import tkinter as tk

# Create a turtle window
window = turtle.Screen()
window.title("Turbo Titans!")  # sets title of window name

# Set the desired window size
window_width = 500
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

# Add your turtle movement code here

# Keep the window open until it is manually closed
turtle.mainloop()
