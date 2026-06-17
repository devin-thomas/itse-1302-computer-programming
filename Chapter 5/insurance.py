#Devin Thomas
#ITSE 1302-003
#June 26, 2023

# This function introduces the user to what the program does.
def intro():
    print("This program calculates the minimum amount of insurance you should buy for your property.")

# This function gets the replacement cost from the user.
def get_cost():
    while True:
        try:
            cost = float(input("Enter the replacement cost of the building: $"))
            if cost < 0:
                print("Invalid input. Please enter a positive number.")
            else:
                return cost
        except ValueError:
            print("Invalid input. Please enter a number.")

# This function calculates the minimum insurance.
def calc_insurance(cost):
    return cost * 0.8

# This function displays the calculated insurance.
def show_calc(insurance):
    print(f"Minimum amount of insurance you should buy: ${insurance:.2f}")

# This function runs the program.
def main():
    intro()
    cost = get_cost()
    insurance = calc_insurance(cost)
    show_calc(insurance)

# Run the program
main()
