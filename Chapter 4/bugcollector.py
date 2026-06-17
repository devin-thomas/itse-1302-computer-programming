#Devin Thomas
#ITSE 1302-003
#June 21, 2023

# Initialize the total number of bugs to 0.
total_bugs = 0

# This loop will run 7 times, one for each day.
for day in range(1, 8):
    while True:  # Start an infinite loop.
        try:
            # Prompt the user to enter the number of bugs collected on this day.
            bugs = int(input(f"Enter the number of bugs collected on day {day}: "))
            
            if bugs < 0:
                print("Number of bugs cannot be negative. Try again.")
            else:
                # If the user entered a valid number, exit the loop.
                break
        except ValueError:
            # If the user entered a non-integer, display an error message and continue to the next iteration.
            print("Invalid input. Please enter a whole number.")
    
    # Add the number of bugs collected on this day to the total.
    total_bugs += bugs

# After the loop is finished, display the total number of bugs collected.
print("The total number of bugs collected is", total_bugs)
