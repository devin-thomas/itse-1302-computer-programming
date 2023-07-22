#Devin Thomas
#ITSE 1302-003
#June 21, 2023

#This program allows the user to mix primary colors and determine the secondary color of the output.

# First, we define the valid colors
valid_colors = ["red", "blue", "yellow"]

# This function gets the color from the user, forces it to lowercase and checks for errors
def get_color_input(prompt):
    color = input(prompt).lower()
    while color not in valid_colors:
        print("Invalid color. Please enter red, blue, or yellow.")
        color = input(prompt).lower()
    return color

# Get the first and second primary colors
color1 = get_color_input("Enter the first primary color: ")
color2 = get_color_input("Enter the second primary color: ")

# Check if the two colors are the same
while color1 == color2:
    print("Same color entered twice. Please enter a different second color.")
    color2 = get_color_input("Enter the second primary color: ")

# Determine the resulting color based on the primary colors
if color1 == "red":
    if color2 == "blue":
        print("The secondary color is purple.")
    elif color2 == "yellow":
        print("The secondary color is orange.")
elif color1 == "blue":
    if color2 == "red":
        print("The secondary color is purple.")
    elif color2 == "yellow":
        print("The secondary color is green.")
elif color1 == "yellow":
    if color2 == "red":
        print("The secondary color is orange.")
    elif color2 == "blue":
        print("The secondary color is green.")
