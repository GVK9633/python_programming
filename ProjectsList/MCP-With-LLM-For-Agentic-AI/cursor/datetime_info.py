from datetime import datetime

# Get current date and time
now = datetime.now()

# Display various date and time formats
print("Current Date and Time:")
print(f"Full datetime: {now}")
print(f"Date only: {now.date()}")
print(f"Time only: {now.time()}")
print(f"Year: {now.year}")
print(f"Month: {now.month}")
print(f"Day: {now.day}")
print(f"Hour: {now.hour}")
print(f"Minute: {now.minute}")
print(f"Second: {now.second}")
print(f"Microsecond: {now.microsecond}")
print(f"Weekday (0-6, Monday is 0): {now.weekday()}")
print(f"ISO format: {now.isoformat()}") 