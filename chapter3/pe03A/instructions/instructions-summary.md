<!-- practice -->
# Aim
Now we will look at a practical use of the while statement.

# Steps for Completion

1. Open *main.py* then declare a variable called `current` and set its value to **1**, as shown in *Snippet 3.14*:

```python
current = 1
```
<sup>*Snippet 3.14*</sup>

2. Declare the `end` variable and set its value to **10**, as shown in *Snippet 3.15*:

```python
end = 10
```
<sup>*Snippet 3.15*</sup>

3. Then, write a `while` statement. The condition of this `while` statement is that the current number is less than or equal to the end number as shown in *Snippet 3.16*:

```python
while current <= end:
```
<sup>*Snippet 3.16*</sup>

4. For every `current` number, print it out and then increment it by **1**, as shown in *Snippet 3.17*:

```python
    print(current)
    current += 1
```
<sup>*Snippet 3.17*</sup>

5. If immediately the condition is not true, print the statement **You have reached the end** as shown in *Snippet 3.18*:

```python
else:
  print('You have reached the end')
```
<sup>*Snippet 3.18*</sup>

Note that the statement **You have reached the end** is printed out only once. This demonstrates how to implement the `else` clause with a `while` statement.

*Snippet 3.19* shows the final code with comments added:

```python
# Set the starting value
current = 1
# Set the end value
end = 10

# While the current number is less than or equal to the end number
while current <= end:
  # Print the current number
  print(current)
  # Increment the current number by one
  current += 1
else:
  """
  Immediately the current number is not less than or equal to the end number, print this statement. Note that the statement is only printed out once
  """
  print('You have reached the end')
```
<sup>*Snippet 3.19*</sup>

6. Finally, run the script. The output of this code is shown in *Snippet 3.20*:

```
$ python3 main.py
1
2
3
4
5
6
7
8
9
10
You have reached the end
```
<sup>*Snippet 3.20*</sup>

As expected, Python loops through all numbers from 1 to 10 and prints them out to standard output. At the end of the loop, the program prints the line `You have reached the end` as expected. This marks the end of program execution, and the program exits.
