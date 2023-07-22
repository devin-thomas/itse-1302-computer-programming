#Devin Thomas
#ITSE 1302-003
#June 21, 2023

# This program creates a table of values based on speed, time and distance.

# Prompt the user to enter the speed of the vehicle and the number of hours traveled
# If the input is less than 0, the user is prompted again for a value.
while True:
    try:
        speed = float(input("Enter the speed of the vehicle (in miles per hour): "))
        if speed < 0:
            raise ValueError("Speed should be a positive number.")
        break
    except ValueError as e:
        print("Invalid input:", e)
        continue

# Prompt the user for the number of hours.
# This value must be a positive integer, and will prompt again if not.
while True:
    try:
        hours = float(input("Enter the number of hours traveled: "))
        if hours <= 0 or hours != int(hours):
            raise ValueError("Hours should be a positive integer.")
        break
    except ValueError as e:
        print("Invalid input:", e)
        continue

# The loop calculates the distance, truncates the value to one decimal point,
# and uses tabs for spacing purposes.
print("Hour\tDistance Traveled")
print("-------------------------")

for hour in range(1, int(hours)+1):
    distance = speed * hour
    print(f"{hour}\t{distance:.1f}")



