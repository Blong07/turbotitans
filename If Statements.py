def carnumber():
    carnumberString = turtle.textinput("Enter car between 1 and " + str(number_of_cars), "Enter Car Number")

    try:

        carnumberX = int(carnumberString)

        # print(str(carnumberX) + " is a good car")

        # car selection (choose between 1 - number of cars)
        if carnumberX >= 1 and carnumberX <= number_of_cars:
            chosen_car(carnumberX)
        else:
            # print('you are annoying and stupid')
            bad_car(carnumberX)

            # show a message box that says you have the wrong car
    except:
        bad_car(carnumberString)