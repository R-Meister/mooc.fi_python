# Write your solution here
year = int(input("Year: "))
currentyear = year
while True:
    year+=1
    if year%4 == 0 and year % 100 == 0 and year % 400 == 0:
        isLeapYear = True
    elif year%4 == 0 and year % 100 != 0 and year % 400 != 0:
        isLeapYear = True
    elif year%4 == 0 and year % 100 == 0 and year % 400 != 0:
        isLeapYear = False
    else:
        isLeapYear = False
    if isLeapYear == True:
        break
print(f"The next leap year after {currentyear} is {year}")