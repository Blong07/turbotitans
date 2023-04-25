import random
import easygui

# Set the initial position of the cars
car1_position = -200
car2_position = -200

# Set the winning parameter to 150 by default
winning_parameter = 150

# Function to display a pop-up dialog box for setting the winning parameter
def set_winning_parameter():
    global winning_parameter
    msg = "Enter the winning parameter (multiple of 50):"
    title = "Set Winning Parameter"
    default_value = str(winning_parameter)
    winning_parameter_str = easygui.enterbox(msg, title, default_value)
    if winning_parameter_str:
        winning_parameter = int(winning_parameter_str)
        if winning_parameter <= 0 or winning_parameter % 50 != 0:
            easygui.msgbox("Winning parameter must be a positive multiple of 50.", "Error")
            set_winning_parameter()

# Function to print the current positions of the cars
def print_positions():
    print("Car 1:", car1_position)
    print("Car 2:", car2_position)

# Function to check if a car has won
def check_winner():
    if car1_position >= winning_parameter:
        return 1
    elif car2_position >= winning_parameter:
        return 2
    else:
        return 0

# Game loop
while True:
    # Move the cars
    car1_position += random.randint(1, 5) * 10
    car2_position += random.randint(1, 5) * 10

    # Print the current positions of the cars
    print_positions()

    # Check if a car has won
    winner = check_winner()
    if winner == 1:
        print("Car 1 wins!")
        break
    elif winner == 2:
        print("Car 2 wins!")
        break

    # Ask the user if they want to set a new winning parameter
    set_winning_parameter()
