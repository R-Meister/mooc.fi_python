# Write your solution here
strin = input("Please type in a string: ")
last = (len(strin))
print(last)
while True:
    if last <= 0:
        break
    else:
        last -= 1
    print(strin[last])

