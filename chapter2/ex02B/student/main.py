word = input("What word do you want to convert? ")
count = int(input("How many letters at the end should be uppercase? "))

pivot = len(word) - count

head = word[:pivot]
tail = word[pivot:]

print(head + tail.upper())