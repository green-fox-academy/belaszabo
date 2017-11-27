current_hours = 14
current_minutes = 34
current_seconds = 42

# Write a program that prints the remaining seconds (as an integer) from a
# day if the current time is represented bt the variables
seconds = 60 - current_seconds
print (seconds)
minutes = 60 - current_minutes - 1
print (minutes)
hours = 24 - current_hours - 1
print (hours)

left = seconds + minutes * 60 + hours * 3600
print(left)