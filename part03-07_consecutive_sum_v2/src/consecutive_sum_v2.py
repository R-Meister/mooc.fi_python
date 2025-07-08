# Write your solution here
# Write your solution here
num = 1
numsum = 0
sum = ""
lim = int(input("Limit: "))
while lim > numsum:
    numsum = numsum + num
    if numsum >= lim:
            sum += (f"{num} ")
    else:
        sum += (f"{num} + ")
        num+= 1
print(f"The consecutive sum: {sum}= {numsum}")
