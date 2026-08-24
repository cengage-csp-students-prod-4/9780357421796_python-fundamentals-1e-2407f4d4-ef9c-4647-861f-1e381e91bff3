# Scenario

Given a list, an array, or other data structure that includes a number of different data types, you want to be able to filter out all of the integers and give an output of the remaining bits of data.

# Aim

Write a function that receives a number of arguments; using a `continue` statement, skip integers and print out all other values.

# Steps for Completion

1. Define a function named `skip_integers`, with a variable number of arguments.

2. Use a `for` loop to iterate over the arguments.

3. Use a check to see whether the value passed is of the integer type. If it is, use the `continue` statement to ignore it.

4. Print the arguments.

The output should be as shown in _Snippet 4.30_:

```python
5.2
value
6.0
```

<sup>_Snippet 4.30_</sup>
