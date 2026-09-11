name = input("Enter you name: ")
password = input("Enter your password: ")

real_password = "Pas$Word" 

if(password == real_password):
    print(f"Welcome back, {name}")


while(password != real_password):
    print("Incorrect password, try again...")
    password = input("Enter your password: ")
    if(password == real_password):
        print(f"Welcome back, {name}")
