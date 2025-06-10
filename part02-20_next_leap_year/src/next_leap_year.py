# Write your solution here
year = int(input("Year: "))
currentyear1 = year

while True:
    year += 1  
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                isLeapYear = True
                ishundred = True
            else:
                isLeapYear = False
                ishundred = True
        else:
            isLeapYear = True
            ishundred = False
    else:
        isLeapYear = False
        ishundred = False

    if isLeapYear:
        break

if isLeapYear == True and ishundred == True:
    print(f"The next leap year after {currentyear1} is {year}")
elif isLeapYear == True and ishundred == False:
    print(f"The next leap year after {currentyear1} is {year}")
