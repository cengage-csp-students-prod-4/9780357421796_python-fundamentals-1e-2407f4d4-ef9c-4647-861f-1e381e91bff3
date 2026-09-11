name = input("Enter your name: ")
real_password = "Pas$Word"

valid = False
while not valid:
    password = input("Enter your password: ")
    if password == real_password:
        valid = True
    else:
        print("Incorrect password, try again...")

print(f"Welcome back, {name}")