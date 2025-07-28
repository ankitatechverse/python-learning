# Program: Time-based Greeting
# This program prints a greeting (Good morning, afternoon, evening, or night)
# based on the current hour using Python's datetime module.


from datetime import datetime

# Get current hour
hour = datetime.now().hour  

# Print greeting based on time
if hour < 12:
    print("Good morning!")
elif hour < 18:
    print("Good afternoon!")
elif hour < 22:
    print("Good evening!")
else:
    print("Good night!")
