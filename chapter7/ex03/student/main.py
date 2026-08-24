import math

# Write your Wheel class here


# Use this to test your code
if __name__ == "__main__":
    wheel = Wheel(7)
    morewheels = True
    while morewheels:
        radius = float(input("Radius of wheel: "))
        wheel.swap_radius(radius)
        print("Surface area of wheel:", wheel.wheel_area())
        print("Perimeter of wheel:", wheel.wheel_perimeter())
        yn = input('More wheels? Y/N ')
        morewheels = yn == 'y' or yn == 'Y'
