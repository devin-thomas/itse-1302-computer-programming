#Devin Thomas
#ITSE 1302-003
#June 21, 2023

#This program checks how many books were purchased and outputs a 
# string detailing the number of points earned.

# The input function prompts the user for the number of books purchased.
# We take a float input to prevent value errors if the user inputs a float
books_purchased = float(input("Enter the number of books purchased this month: "))

# While loop checks if the input is less than 0. If it is, it prompts the user again.
while books_purchased < 0:
    print("Invalid number. The number of books purchased cannot be less than 0.")
    books_purchased = float(input("Enter the number of books purchased this month: "))

# Truncate the float to an integer.
books_purchased = int(books_purchased)

# If-else structure determines the number of points based on the number of books purchased.
if books_purchased == 0:
    points = 0
elif books_purchased == 1:
    points = 5
elif books_purchased == 2:
    points = 15
elif books_purchased == 3:
    points = 30
else:
    points = 60

# Print the number of points.
print("The number of points awarded is", points)