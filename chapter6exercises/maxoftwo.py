#Devin Thomas
#ITSE 1302-003
#June 27, 2023

def intro():
    # Inform the user about the program
    print("This program accepts two integer values and returns the value that is the greater of the two.")

def get_ints():
    # Prompt the user to enter two integer values
    values = []
    for i in range(2):
        while True:
            try:
                value = int(input(f"Enter integer value {i+1}: "))
                values.append(value)
                break
            except ValueError:
                print("Invalid input. Please enter an integer value.")
    return values

def find_max(values):
    # This function is designed to replicate the max() function which is built into python
    if values[0] > values[1]:
        return values[0]
    else:
        return values[1]

def show_max(max_value):
    # Display the maximum value
    print(f"The greater value is: {max_value}")

def main():
    # Main function to control the program flow
    intro()
    values = get_ints()
    max_value = find_max(values)
    show_max(max_value)

# Run the program
main()
