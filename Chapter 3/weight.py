#Devin Thomas
#ITSE 1302-003
#June 18, 2023

# This program calculates an object's weight in Newtons based on its mass.

# The user is prompted to enter the object's mass in kilograms.
mass = float(input("Enter the object's mass in kilograms: "))

# The weight is calculated using the formula Weight = Mass x 9.8
weight = mass * 9.8

# The weight is printed.
print("The weight of the object is", weight, "Newtons.")

# If the weight is greater than 1000 Newtons, a message is printed indicating that the object is too heavy.
if weight > 1000:
    print("The object is too heavy.")
# If the weight is less than 10 Newtons, a message is printed indicating that the object is too light.
elif weight < 10:
    print("The object is too light.")
