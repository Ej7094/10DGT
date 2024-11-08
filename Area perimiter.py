enter = ""
while enter == "":
    # Making the input a number more than zero
    error = "Please enter a number that is more than zero"

    def test1():
        while True:
            try:
                num_1 = int(input("First give me the length of the rectangle "))
                if num_1 > 0:
                    return num_1
                else:
                    print(error)
            except ValueError:
                print("you dumb kid give me number")
              
# Second one for the second number
    def test2():
        while True:
            try:
                num_2 = int(input("Next give me the whidth of the rectangle "))
                if num_2 > 0:
                    return num_2
                else:
                    print(error)
            except ValueError:
                print("you dumb kid give me number") 
# Saying what the user is making
    print("You're going to make a rectangle")
    num1 = test1()
    num2 = test2()
# Once the numbers are entered, calculate the area
    print("Next we are going to calculate the area of your rectangle ")
    sum = num1 * num2
# Next calculate the perimeter
    print(sum)
    print("Then we are going to calculate the perimeter of the rectangle")
    print("The perimeter of the rectangle is ")    
    perimeter = num1 + num2 + num1 + num2
    print(perimeter)
# Asking if the user wants to do it again if not then quit
# Press enter to loop
    print("Would you like to do this again with a different number?")
    enter = input ("press <enter> to do this again press anything else to stop ")
