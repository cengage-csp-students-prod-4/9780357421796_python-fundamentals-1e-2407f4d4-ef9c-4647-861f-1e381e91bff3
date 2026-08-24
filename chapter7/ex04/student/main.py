# Write your Package class here


# This is to test your code
if __name__ == '__main__':
    morepackages = True
    while morepackages:
        items = int(input("How many items are in the package?: "))
        package = Package(items)
        yn = input('Ship more packages? Y/N ')
        morepackages = yn == 'y' or yn == 'Y'
