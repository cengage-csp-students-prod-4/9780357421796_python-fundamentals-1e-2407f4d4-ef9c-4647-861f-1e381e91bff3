user_input_string = input("Sentence: ")
word_to_look_for = input("Word to look for in sentence: ")

clean_string = str.strip(str.lower(user_input_string))


occurances = clean_string.count(word_to_look_for)

print(f"There are {occurances} occurances of '{word_to_look_for}' in the sentence.")

