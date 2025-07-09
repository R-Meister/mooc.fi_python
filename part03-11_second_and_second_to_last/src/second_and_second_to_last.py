# Write your solution here
strin = input("Please type in a string: ")
sec = strin[1]
last = strin[-2]
if sec == last:
    print(f"The second and the second to last characters are {sec}")
elif sec != last:
    print("The second and the second to last characters are different")