#Devin Thomas
#ITSE 1302-003
#June 26, 2023

# This function prompts the user to enter a distance in kilometers.
def get_km():
    while True:
        try:
            input_km = float(input("Enter a distance in kilometers: "))
            return input_km
        except ValueError:
            print("Invalid input. Please enter a number.")

# This function converts the distance from kilometers to miles.
def km_to_mi(km):
    return km * 0.6214

# This function prints the converted distance in miles.
def print_mi(miles):
    print(f"The distance in miles is {miles:.4f}.")

# This is the main function that runs the program.
def main():
    km = get_km()
    mi = km_to_mi(km)
    print_mi(mi)

# Run the program
main()
