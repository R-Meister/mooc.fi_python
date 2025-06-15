# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
count = 0
sum = 0
pcount = 0
ncount = 0
mean = 0
while True:
    num = int(input("Number: "))
    if num == 0:
        break
    sum += num
    count +=1
    if num < 0:
        ncount += 1
    elif num > 0:
        pcount += 1
    mean = float(sum/count)
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {pcount}")
print(f"Negative numbers {ncount}")

