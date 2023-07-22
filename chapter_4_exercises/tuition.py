#Devin Thomas
#ITSE 1302-003
#June 21, 2023

# Initialize the tuition amount for the first semester
tuition = 6000

# Display the header for the tuition projection
print(f"Based on the current tuition of {tuition}, here is the tuition projection for the next five years:")

# Use a for loop to iterate over the next five years
for year in range(1, 6):
    # Calculate the tuition increase for the current year
    tuition_increase = tuition * 0.02
    
    # Update the tuition amount for the next year
    tuition += tuition_increase
    
    # Display the projected tuition amount for the current year
    print(f"Year {year}: ${tuition:.2f}")

