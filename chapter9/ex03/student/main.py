import random

# Write your error handling block here

try:
    print(random.randinteger(5,15))

except AttributeError:
    print("Double check the attributes in your code and try again.")
except Exception:
    print("exception occured idk why tho")


print("outside of the try block")