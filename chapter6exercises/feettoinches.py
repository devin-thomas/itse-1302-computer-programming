#Devin Thomas
#ITSE 1302-003
#June 27, 2023

def intro():
    # Inform the user of the purpose of the program.
    print("This program converts feet to inches.")

def get_feet():
    # Prompt the user to enter a number of feet.
    while True:
        try:
            feet = float(input("Enter the number of feet: "))
            return feet
        except ValueError:
            print("Invalid input. Please enter a number.")

def feetToInches(feet):
    # Convert the number of feet to inches.
    return feet * 12

def show_inches(inches):
    # Display the number of inches.
    print(f"That is {inches:.1f} inches.")

def main():
    intro()
    feet = get_feet()
    inches = feetToInches(feet)
    show_inches(inches)

# Run the program
main()
