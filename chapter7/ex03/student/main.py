import math

# Write your Wheel class here

class Wheel:
    def __init__(self, radius):
        self.radius = radius

    def wheel_area(self, radius):
        self.area = math.pi * radius ** 2
        return self.area

    def wheel_perimeter(self, radius):
        self.perimeter = 2 * math.pi * radius
        return self.area

    def swap_radius(self, radius):
        self.radius = radius

    


# Use this to test your code
if __name__ == "__main__":
    wheel = Wheel(7)
    morewheels = True
    while morewheels:
        radius = float(input("Radius of wheel: "))
        wheel.swap_radius(radius)
        print("Surface area of wheel:", wheel.wheel_area(radius))
        print("Perimeter of wheel:", wheel.wheel_perimeter(radius))
        yn = input('More wheels? Y/N ')
        morewheels = yn == 'y' or yn == 'Y'
