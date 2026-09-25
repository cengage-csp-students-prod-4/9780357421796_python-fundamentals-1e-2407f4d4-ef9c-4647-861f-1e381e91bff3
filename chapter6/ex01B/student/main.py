def word_counter(word):

    occurances = dict()

    for char in word:
        if(char == " "): continue
        if(char in occurances):
            occurances[char] += 1
        else:
            occurances[char] = 1

    return occurances

print(word_counter("Mississippi")) 