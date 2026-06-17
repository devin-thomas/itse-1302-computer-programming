#Devin Thomas
#ITSE 1302-003
#June 26, 2023

def intro():
    # Inform the user of the purpose of the program
    print("This program calculates a person's Body Mass Index (BMI).")

def get_stats():
    # Prompt the user to enter the weight and height
    while True:
        try:
            weight = float(input("Enter your weight in lbs: "))
            if weight < 0:
                print("Invalid input. Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
            
    while True:
        try:
            height = float(input("Enter your height in inches: "))
            if height < 0:
                print("Invalid input. Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    return weight, height

def calc(weight, height):
    # Calculate the Body Mass Index (BMI)
    bmi = weight * 703 / height**2
    return bmi

def show_calc(bmi):
    # Display the Body Mass Index (BMI)
    print(f"Your BMI is: {bmi:.2f}")

def main():
    intro()
    weight, height = get_stats()
    bmi = calc(weight, height)
    show_calc(bmi)

# Run the program
main()
