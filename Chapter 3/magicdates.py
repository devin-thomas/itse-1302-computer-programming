#Devin Thomas
#ITSE 1302-003
#June 18, 2023

# This program determines whether a given date is "magic".

# The user is prompted to enter the month, day, and year of a date.
month = int(input("Enter the month (in numeric form, 1-12): "))
while month < 1 or month > 12:
    print("Invalid month. Please enter a value between 1 and 12.")
    month = int(input("Enter the month (in numeric form, 1-12): "))

# Each month has maximum date values assigned. More on February 29th later.
if month in [4, 6, 9, 11]:
    max_day = 30
elif month == 2:
    max_day = 29
else:
    max_day = 31

day = int(input(f"Enter the day (1-{max_day}): "))
while day < 1 or day > max_day:
    print(f"Invalid day. Please enter a value between 1 and {max_day}.")
    day = int(input(f"Enter the day (1-{max_day}): "))

# The program checks that the year is between 0 and 99.
year = int(input("Enter the year (two digits): "))
while year < 0 or year > 99:
    print("Invalid year. Please enter a two-digit year between 0 and 99.")
    year = int(input("Enter the year (two digits): "))
    

# The product of the month and day is calculated.
product = month * day

# Check for special case of Feb 29 and non-leap year
if month == 2 and day == 29 and year % 4 != 0:
    print("Note: February 29 does not occur in non-leap years.")

# If the product equals the year, the date is magic.
if product == year:
    print("The date is magic.")
else:
    print("The date is not magic.")
