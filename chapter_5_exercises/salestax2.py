#Devin Thomas
#ITSE 1302-003
#June 26, 2023

# This function introduces the user to what the program does.
def intro():
    print("This program calculates the total sale price, including state and county tax.")

# This function gets the purchase amount from the user.
def get_price():
    while True:
        try:
            price = float(input("Enter the purchase amount: $"))
            return price
        except ValueError:
            print("Invalid input. Please enter a number.")

# This function calculates the state tax.
def calc_state_tax(price):
    return price * 0.04

# This function calculates the county tax.
def calc_county_tax(price):
    return price * 0.02

# This function calculates the combined tax.
def calc_combined_tax(state_tax, county_tax):
    return state_tax + county_tax

# This function calculates the total sale price.
def calc_total(price, total_tax):
    return price + total_tax

# This function displays the calculations.
def show_calcs(price, state_tax, county_tax, total_tax, total_sale):
    print(f"Purchase Amount: ${price:.2f}")
    print(f"State Sales Tax: ${state_tax:.2f}")
    print(f"County Sales Tax: ${county_tax:.2f}")
    print(f"Total Sales Tax: ${total_tax:.2f}")
    print(f"Total Sale: ${total_sale:.2f}")

# This function runs the program.
def main():
    intro()
    price = get_price()
    state_tax = calc_state_tax(price)
    county_tax = calc_county_tax(price)
    total_tax = calc_combined_tax(state_tax, county_tax)
    total_sale = calc_total(price, total_tax)
    show_calcs(price, state_tax, county_tax, total_tax, total_sale)

# Run the program
main()
