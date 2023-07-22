#Devin Thomas
#ITSE 1302-003
#June 28, 2023

def main():
    # Cost per seat for each section
    cost_a = 20
    cost_b = 15
    cost_c = 10

    # Maximum seats available for each section
    max_a = 300
    max_b = 500
    max_c = 200

    # Minimum seats
    min_seats = 0

    # Inform the user of the purpose of the program
    print("This program calculates the total income generated from ticket sales in a theater.")
    print("Please enter the number of tickets sold for each section.")

    # Get the number of seats sold for each section
    a = get_seats(max_a, min_seats, 'A')
    b = get_seats(max_b, min_seats, 'B')
    c = get_seats(max_c, min_seats, 'C')

    # Calculate the total income
    income_full = calc_income(a, b, c, cost_a, cost_b, cost_c)

    # Display the total income
    show_calcs(income_full)

def get_seats(max_seats, min_seats, section):
    while True:
        try:
            # The function accepts a float to reduce error frequency, then converts to an int
            # Decimal values are thrown away as there are no partial seats
            seats = int(float(input(f"Enter the number of tickets sold in section {section}: ")))
            if seats < min_seats or seats > max_seats:
                print(f"Invalid input. Please enter a number between {min_seats} and {max_seats}.")
            else:
                return seats
        except ValueError:
            print("Invalid input. Please enter a number.")

def calc_income(a, b, c, cost_a, cost_b, cost_c):
    return (a * cost_a) + (b * cost_b) + (c * cost_c)

def show_calcs(income_full):
    print(f"The total income from ticket sales is: ${income_full:.2f}")

# Run the program
main()
