<!-- practice -->
# Aim
In this exercise, we will utilize nested loops to print out the numbers **1** through **9** with their squares. 

# Steps for Completion

1. Open *main.py*, then, create a variable called `groups`, which is a list that contains three other lists of three integers each as shown in *Snippet 3.51*:

```python
groups = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
<sup>*Snippet 3.51*</sup>

From the structure of the list, it is clear that just looping over it will not get us to the individual integers. To get to the individual integers, we have to loop over the groups and then loop over each group.

2. Loop over `groups` as shown in *Snippet 3.52*:

```python
for group in groups:
```
<sup>*Snippet 3.52*</sup>

3. For each `group`, loop over it to reach the individual integers, which we call `num` as shown in *Snippet 3.53*:

```python 
	for num in group:
```
<sup>*Snippet 3.53*</sup>

4. Then, proceed to calculate the square of each number as shown in *Snippet 3.54*:

```python
		square = num * num
```
<sup>*Snippet 3.54*</sup>

5. Finally, print out the statement that shows the number's square as shown in *Snippet 3.55*:

```python
		print(num ,' squared is ', square)
```
<sup>*Snippet 3.55*</sup>

*Snippet 3.56* shows the final code with comments for clarification:

```python
# Create a list with three groups of numbers 1 through 9
groups = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Loop through the list of number groups
for group in groups:
# Loop through numbers in group
    for num in group:
# Calculate the square of the number
        square = num * num
# Print out a string showing the num
        print(num ,' squared is ', square)
```
<sup>*Snippet 3.56*</sup>

6. Run the script. The output of the preceding code is shown in *Snippet 3.57*:

```
$ python3 main.py

1 squared is 1
2 squared is 4
3 squared is 9
4 squared is 16
5 squared is 25
6 squared is 36
7 squared is 49
8 squared is 64
9 squared is 81
```
<sup>*Snippet 3.57*</sup>

As you can see, we are able to loop over the individual groups of integers and perform calculations on the individual integers by nesting the `for` loops. This is the power of nesting: it can allow us to unpack complex structures.

