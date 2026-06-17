import datetime

# Get the current date and time
now = datetime.datetime.now()
print(now)

# Create a specific datetime
birthday = datetime.datetime(1996, 1, 15)
print(birthday)

# Calculate the difference between two dates
age = now - birthday
print(age.days)
