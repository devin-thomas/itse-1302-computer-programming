#Devin Thomas
#ITSE 1302-003
#June 26, 2023

def intro():
    # Inform the user of the purpose of the program
    print("This program calculates the assessment value and property tax of a piece of property.")

def get_value():
    # Prompt the user to enter the actual value of the property
    while True:
        try:
            actual_value = float(input("Enter the actual value of the property: $"))
            if actual_value < 0:
                print("Invalid input. Please enter a positive number.")
            else:
                return actual_value
        except ValueError:
            print("Invalid input. Please enter a number.")

def calc(actual_value):
    # Calculate the assessment value and property tax
    assessment_value = actual_value * 0.60
    property_tax = assessment_value * 0.0064
    return assessment_value, property_tax

def show_calcs(assessment_value, property_tax):
    # Display the assessment value and property tax
    print(f"Assessment value: ${assessment_value:.2f}")
    print(f"Property tax: ${property_tax:.2f}")

def main():
    intro()
    actual_value = get_value()
    assessment_value, property_tax = calc(actual_value)
    show_calcs(assessment_value, property_tax)

# Run the program
main()
