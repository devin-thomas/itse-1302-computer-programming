#Devin Thomas
#ITSE 1302-003
#June 21, 2023

# This program asks for a series of positive numbers from the user and keeps a running total, 
# which is displayed at the end.

# initialize the total value.
total = 0

while True:
    try:
        number = float(input("Enter a positive number (or a negative number to finish): "))
        
        # If the number is negative, break out of the loop. This is the signal to end the series.
        if number < 0:
            break
        
        # Add the number to the total.
        total += number
    
    # Handle the ValueError exception if the input cannot be converted to a float.
    except ValueError:
        print("Invalid input. Please enter a positive number.")
        continue

# Once the loop has finished (i.e., the user has entered a negative number), print the total.
print("The total is", total)
