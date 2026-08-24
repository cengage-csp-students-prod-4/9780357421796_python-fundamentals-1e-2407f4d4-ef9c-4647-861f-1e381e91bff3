<!-- practice -->
# Aim
To show the power of `while` loops, let's look at an example that uses a `while` loop to keep an interactive Python program running until a condition is met. To do this, we will rewrite the program we wrote in *Program Exercise 3-2* and add a `while` statement.

The `while` loop is used in the following cases:

• When we must wait for a condition to be satisfied before continuing execution

• When a user's input is required—as seen in the second example code snippet

# Steps for Completion

1. Open *main.py* and set `release_year` to **1991** as shown in *Snippet 3.21*. This is the correct answer to the question that is going to be asked:

```python
release_year = '1991'
```
<sup>*Snippet 3.21*</sup>

2. Next, set the `correct` condition to `False` as shown in *Snippet 3.22*. We will be using this condition to check whether we should break out of the `while` statement:

```python
correct = False
```
<sup>*Snippet 3.22*</sup>

3. Now go into the body of the `while` statement. While the answer provided is not correct, keep the program running. Notice that we use a negative condition, where we check whether the provided answer is incorrect. Implement this as shown in *Snippet 3.23*:

```python
while not correct:
```
<sup>*Snippet 3.23*</sup>

4. Print out the question as shown in *Snipper 3.24*:

```python
	answer = input('When was Python first released? ')
```
<sup>*Snippet 3.24*</sup>

Note the use of `input()`. This tells the terminal to wait for user keyboard input.

5. Use an `if` statement to check that the provided answer is correct as shown in *Snippet 3.25*:

```python
	if answer == release_year:
```
<sup>*Snippet 3.25*</sup>

6. If the answer is correct, print a success message to the terminal as shown in *Snippet 3.26*:

```python
		print('Congratulations! That is correct.')
```
<sup>*Snippet 3.26*</sup>

7. After printing the message, set `correct` to **True** as shown in *Snippet 3.27*. This will cause the `while` loop to stop executing:

```python
		correct = True
```
<sup>*Snippet 3.27*</sup>

8. If the answer is incorrect, encourage the user to try again as shown in *Snippet 3.28*:

```python
	else:
	    print('No, that\'s not it. Try again\n')
```
<sup>*Snippet 3.28*</sup>

9. Lastly, print the exit message as shown in *Snippet 3.29*:

```python
print('Bye!')
```
<sup>*Snippet 3.29*</sup>

*Snippet 3.30* shows the final code. Comments have been added for clarification:

```python
# Set release_year to 1991. This is the correct answer to the question to be asked
# Note that this is a string as user input is automatically set to type str
release_year = '1991'
# Set the condition "correct" to False
correct = False

# While the answer provided is not correct, keep the program running
while not correct:
  # Print out the question to stdout
  # Note the use of input(). This tells the terminal to wait for user keyboard input
  answer = input('When was Python first released? ')
  
  # Use an if statement to check that the provided answer is correct
  if answer == release_year:
    # If the answer is correct, print success message to stdout
    print('Congratulations! That is correct. ')
    # After printing message, set correct to True
    # This will cause the while loop to stop executing
    correct = True
  else:
    # If the answer is incorrect, encourage user to try again
    print('No, that\'s not it. Try again\n')

# Finally, print the exit message
# Note that this is only printed just before the program exits
print('Bye!')
```
<sup>*Snippet 3.20*</sup>

10. Finally, run the script. *Snippet 3.31* shows the output with incorrect answers first, and then the correct answer:

```
$ python3 main.py

When was Python first released? 1841
No, that's not it. Try again

When was Python first released? 2001
No, that's not it. Try again

When was Python first released? today
No, that's not it. Try again

When was Python first released? 1991
Congratulations! That is correct.
Bye!
```
<sup>*Snippet 3.31*</sup>
