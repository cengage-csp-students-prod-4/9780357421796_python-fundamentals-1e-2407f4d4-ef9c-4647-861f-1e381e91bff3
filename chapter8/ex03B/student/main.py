# Write your function here
def resources_scanner(package):
    resources = dir(package)
    for i in resources:
        print(i)

if __name__ == '__main__':
    import string 
    resources_scanner(string)
