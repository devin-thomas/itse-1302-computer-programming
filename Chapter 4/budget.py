#Devin Thomas
#ITSE 1302-003
#June 21, 2023

# This program tracks a user's monthly budget and expenses.

while True:
    try:
        # Get the budget for the month
        budget = float(input("Enter your budget for the month: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

# Initialize a variable for total expenses
total_expenses = 0.0

# Loop to get each expense
while True:
    try:
        expense = float(input("Enter an expense (or 0 to finish): "))
        if expense == 0:
            break
        total_expenses += expense
    except ValueError:
        print("Invalid input. Please enter a number.")

# Calculate and display the amount the user is over or under budget
difference = budget - total_expenses

if difference < 0:
    print("Your total expenses are ${:.2f} and you are over budget by ${:.2f}".format(total_expenses, -difference))
elif difference > 0:
    print("Your total expenses are ${:.2f} and you are under budget by ${:.2f}".format(total_expenses, difference))
else:
    print("Your total expenses are ${:.2f}. Congratulations, you've perfectly matched your budget!".format(total_expenses))
