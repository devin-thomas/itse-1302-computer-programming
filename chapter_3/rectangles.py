#Devin Thomas
#ITSE 1302-003
#June 18, 2023

# This program compares the area of two rectangles.

# The user is prompted to enter the length and width of the first rectangle.
length1 = float(input("Enter the length of the first rectangle: "))
width1 = float(input("Enter the width of the first rectangle: "))

# The area of the first rectangle is calculated.
area1 = length1 * width1

# The user is prompted to enter the length and width of the second rectangle.
length2 = float(input("Enter the length of the second rectangle: "))
width2 = float(input("Enter the width of the second rectangle: "))

# The area of the second rectangle is calculated.
area2 = length2 * width2

# The areas of both rectangles are printed.
print("Area of the first rectangle: ", area1, "square units.")
print("Area of the second rectangle: ", area2, "square units.")

# The areas of the rectangles are compared and a message is printed accordingly.
if area1 > area2:
    print("The first rectangle has a greater area.")
elif area1 < area2:
    print("The second rectangle has a greater area.")
else:
    print("Both rectangles have the same area.")
