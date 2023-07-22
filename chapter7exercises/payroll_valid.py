#Devin Thomas
#ITSE 1302-003
#June 28, 2023

def main():
    # Introduction
    print("Welcome to the payroll program.")
    print("Please provide the employee's hourly pay rate and hours worked.")

    # Get pay rate and hours worked with input validation
    hourly_rate, hours_worked = get_inputs()

    # Calculate gross pay
    gross_pay = calc_gross_pay(hourly_rate, hours_worked)

    # Display gross pay
    show_gross_pay(gross_pay)

def get_inputs():
    pay_rate = None
    hours = None
    while pay_rate is None:
        try:
            pay_rate = float(input("Enter the hourly pay rate ($7.50 - $18.25): $"))
            if pay_rate < 7.50 or pay_rate > 18.25:
                print("Invalid input. The hourly rate should be between $7.50 and $18.25.")
                pay_rate = None
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    while hours is None:
        try:
            hours = float(input("Enter the number of hours worked (0 - 40): "))
            if hours < 0 or hours > 40:
                print("Invalid input. The hours worked should be between 0 and 40.")
                hours = None
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    return pay_rate, hours

def calc_gross_pay(rate, hours):
    return rate * hours

def show_gross_pay(pay):
    print(f"The employee's gross pay is: ${pay:.2f}")

# Run the program
main()
