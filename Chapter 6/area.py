#Devin Thomas
#ITSE 1302-003
#June 27, 2023

# This program calculates the area of a rectangle.

def intro():
    # Inform the user of the purpose of the program.
    print("This program calculates the area of a rectangle.")

def get_inputs():
    # Prompt the user to enter the width and length of the rectangle.
    while True:
        try:
            width = float(input("Enter the width of the rectangle: "))
            if width <= 0:
                print("Invalid input. Width must be greater than zero.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            length = float(input("Enter the length of the rectangle: "))
            if length <= 0:
                print("Invalid input. Length must be greater than zero.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    return width, length

def calc_area(width, length):
    # Calculate the area of the rectangle.
    return width * length

def show_calc(area):
    # Display the area of the rectangle.
    print(f"The area of the rectangle is {area:.3f} square units.")

def main():
    intro()
    width, length = get_inputs()
    area = calc_area(width, length)
    show_calc(area)

# Run the program
main()
