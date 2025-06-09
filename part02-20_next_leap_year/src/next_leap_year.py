# Write your solution here
year = int(input("Year: "))
while True:
    if year % 4 == 0:
        if year % 100 == 0:
            if year %400 == 0:
                isLeapYear = True
            elif year %400 != 0:
                isLeapYear = False
        else isLeapYear = True
    
    else:
        isLeapYear = False

