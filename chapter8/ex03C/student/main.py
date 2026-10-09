import random

def number_randomizer(num):
    MIN = 0
    MAX = 100

    random_nums = []
    counter = 0
    while counter < num:
        random_nums.append(random.randint(MIN, MAX))
        counter += 1
    return random_nums

print(number_randomizer(2)) 
print(number_randomizer(4))
print(number_randomizer(6))
