# Write your Package class here
class Package:
    LIMIT = 6
    def __init__(self, items):
        if(items > self.LIMIT):
            print(f"""The maximm item limit has been 
                  exceeded. {items - self.LIMIT} items must be 
                   removed from the package """)
        else:
            print(f"There are {items} in the package being shipped out")

# This is to test your code
if __name__ == '__main__':
    morepackages = True
    while morepackages:
        items = int(input("How many items are in the package?: "))
        package = Package(items)
        yn = input('Ship more packages? Y/N ')
        morepackages = yn == 'y' or yn == 'Y'
