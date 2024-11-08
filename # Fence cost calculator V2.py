# Fence cost calculator
# Author: Joshua Bradley
# Date: 8/11/24
# Version 2


def num_check(question):
    # Making the input a number more than zero
    error = "Please enter a number that is more than zero"
    while True:
        try:
            num_1 = int(input(question))
            if num_1 > 0:
                return num_1
            else:
                print(error)
        except ValueError:
            print("you dumb kid give me number")


enter = ""
while enter == "":
              
    # Saying what the user is making
    print("This is a fence cost calculator ")
    width = num_check("Enter the width: ")
    length = num_check("Enter the length: ")
    cost = num_check("Enter the cost $")
    # Asking for the cost of the fencing
    # Calculate the perimeter
    print("We are going to calculate the perimeter of the fencing")
    print("The perimeter of the rectangle is ")    
    perimeter = (width + length) * 2
    print(perimeter)
    # Total cost
    price = cost * perimeter
    print(f"The total price will be ${price}")

    # Asking if the user wants to do it again if not then quit
    # Press enter to loop
    print("Would you like to do this again with a different number?")
    enter = input ("press <enter> to do this again press anything else to stop ")