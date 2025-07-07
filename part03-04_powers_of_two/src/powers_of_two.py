# Write your solution here
up = int(input("Upper limit: "))
num = 0
while (2**num) <= up:
    print(2**num)
    num += 1