#Devin Thomas
#ITSE 1302-003
#June 21, 2023

# This program displays the calories burned after a specific number of minutes at a fixed burn rate.

# Define the constant calories burned per minute
CALORIES_PER_MINUTE = 3.9

# Using a for loop to calculate the calories burned for each minute milestone
for minutes in [10, 15, 20, 25, 30]:
    # Calculate the calories burned
    calories_burned = CALORIES_PER_MINUTE * minutes
    # Display the result
    print(f"After {minutes} minutes, you will have burned {calories_burned} calories.")
