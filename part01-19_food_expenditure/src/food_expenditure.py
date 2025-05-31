# Write your solution here
cafe = int(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
week = float(input("How much money do you spend on groceries in a week? "))
print("")
print("Average food expenditure:")
print(f"Daily: {((cafe*price)+week)/7} euros")
print(f"Weekly: {(cafe*price) + week} euros")
