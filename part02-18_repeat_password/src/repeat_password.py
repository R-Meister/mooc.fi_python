# Write your solution here
passw = input("Password: ")
while True:
    passw_auth = input("Repeat password: ")
    if passw != passw_auth:
        print("They do not match!")
    elif passw == passw_auth:
        print("User account created!")
        break


