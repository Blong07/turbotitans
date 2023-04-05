# importing easygui module
from easygui import *
import easygui

# message / information to be displayed on the screen
message = "Press spacebar to move the cars"

# title of the window
title = "Turbo Titans"

# text of the Ok button
ok_btn_txt = "Continue"

# creating a message box
output = msgbox(message, title, ok_btn_txt)

# printing the output
print("User pressed  : " + output)