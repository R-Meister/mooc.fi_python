# Write your solution here
hour = float(input("Hourly wage: "))
work = int(input("Hours worked: "))
day = input("Day of the week: ")
if day == 'Sunday':
    hour *= 2
print(f"Daily wages: {hour*work} euros")



