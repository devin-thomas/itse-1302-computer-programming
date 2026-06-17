#Devin Thomas
#ITSE 1302-003
#June 14, 2023

# This program converts a number from 1 to 10 into its corresponding Roman numeral.

# A dictionary is created to map numbers to their Roman numeral equivalents.
num_to_roman = {
    1: 'I', 
    2: 'II', 
    3: 'III', 
    4: 'IV', 
    5: 'V', 
    6: 'VI', 
    7: 'VII', 
    8: 'VIII', 
    9: 'IX', 
    10: 'X'
}

# The input function prompts the user for input.
num = int(input("Enter an integer from 1 to 10: "))

# The while loop checks if the input number is outside the range 1 to 10.
while num < 1 or num > 10:
    # If the number is out of range, the program prints an error message.
    print("Error: number is not in the range 1 to 10.")
    # The user is prompted again for a valid value.
    num = int(input("Enter a number from 1 to 10: "))

# If the number is in range, the program prints its Roman numeral equivalent.
print("The Roman numeral is", num_to_roman[num])
