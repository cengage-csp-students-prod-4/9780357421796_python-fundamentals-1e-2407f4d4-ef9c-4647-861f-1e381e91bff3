<!-- practice -->
# Aim

In this exercise, we will see a practical application of the `if` statement:

# Steps for Completion

1. Open _main.py_ and declare a variable of type `string` called `release_year` and assign the value **1991** to it as shown in _Snippet 3.2_:

```python
release_year = '1991'
```

<sup>_Snippet 3.2_</sup>

2. Then, declare another variable called `answer` and assign it to an input function call as shown in _Snippet 3.3_:

```python
answer = input('When was Python first released? ')
```

<sup>_Snippet 3.3_</sup>

3. Next, use an `if` statement to check whether the answer entered by the user is correct. If the answer is correct, we print out the success message `Congratulations! That is correct.`. The `if` statement is shown in _Snippet 3.4_:

```python
if answer == release_year:
	print('Congratulations! That is correct.')
```

<sup>_Snippet 3.4_</sup>

4. Then, use an `elif` statement to check whether the answer entered by the user is greater than the correct answer. `elif` is a combination of `else` and `if`, and enables a broader comparison scope through chaining multiple `if` statements. If the answer is greater than the correct answer, we tell the user that the guess was too high as shown in _Snippet 3.5_:

```python
elif answer > release_year:
	print('No, that\'s too late')
```

<sup>_Snippet 3.5_</sup>

5. Next, use an `elif` to check whether the answer entered by the user is less than the correct answer. If the answer is less than the correct answer, we tell the user that the guess was too low as shown in _Snippet 3.6_:

```python
elif answer < release_year:
	print('No, that\'s too early')
```

<sup>_Snippet 3.6_</sup>

6. Finally, print the exit message as shown _Snippet 3.7_:

```python
print('Bye!')
```

<sup>_Snippet 3.7_</sup>

_Snippet 3.8_ shows the final code for the script. Please note comments are included for clarification:

```python
# Set release_year to 1991
release_year = '1991'
# Prompt the user to enter their answer to the question
answer = input('When was Python first released? ')

if answer == release_year:
  # If the answer is correct, show the success message
  print('Congratulations! That is correct.')
elif answer > release_year:
  # If the answer is greater that release_year, tell the user the guess was too high
  print('No, that\'s too late')
elif answer < release_year:
  # If the answer is less that release_year, tell the user the guess was too low
  print('No, that\'s too early')

# Finally, print the exit message
print('Bye!')
```

<sup>_Snippet 3.8_</sup>

Now let's look at some sample output from running this program and giving it various responses:

7. First, we'll look at what happens when you give the program an answer that is less than the expected answer. Run the script in the terminal and on being prompted, enter an incorrect value, such as **1969**, as shown in _Snippet 3.9_:

```
When was Python first released? 1969
No, that's too early
Bye!
```

<sup>_Snippet 3.9_</sup>

8. The output in _Snippet 3.10_ shows what happens when you provide the correct answer to the program. Run the script again and enter **1991** as the input:

```
When was Python first released? 1991
Congratulations! That is correct.
Bye!
```

<sup>_Snippet 3.10_</sup>
