<!-- pratice -->

# Aim

Assign an integer to a variable and then perform mathematical operations with the variable.

# Steps for Completion

1. Assign the value `7` to the `number` variable as shown in _Snippet 1.24_:

```
>>> number = 7
```

<sup>_Snippet 1.24_</sup>

2. We can now use this variable for any operations we'd like. Print out the value of the `number` variable, multiplied by `5` as shown in _Snippet 1.25_:

```
>>> number * 5
35
```

<sup>_Snippet 1.25_</sup>

3. Print out `number` added to `2` as shown in _Snippet 1.26_:

```
>>> number + 2
9
```

<sup>_Snippet 1.26_</sup>

4. Print out `number` divided by `3.5` as shown in _Snippet 1.27_:

```
>>> number / 3.5
2.0
```

<sup>_Snippet 1.27_</sup>

5. Print out `number` subtracted from itself as shown in _Snippet 1.28_:

```
>>> number - number
0
```

<sup>_Snippet 1.28_</sup>

6. Note that, despite having used it, the value of `number` won't change unless we reassign it. Reassigning `22` to `number` changes its value as shown in _Snippet 1.29_:

```
>>> print(number)
7
>>> number = 22
>>> print(number)
22
>>>
```

<sup>_Snippet 1.29_<sup>

7. You can also assign the resulting value of another operation to a variable. Enter the commands shown in _Snippet 1.30_:

```
>>> number = 7
>>> x = number + 1
>>> x
8
>>>
```

<sup>_Snippet 1.30_</sup>

8. String values can also be assigned and used in a similar fashion. First, set the `message` variable to the string `"I love Python"` as shown in _Snippet 1.31_:

```
>>> message = "I love Python"
```

<sup>_Snippet 1.31_</sup>

9. Print out the value of the `message` variable and add an exclamation point at the end as shown in _Snippet 1.32_:

```
>>> message + "!"
'I love Python!'
```

<sup>_Snippet 1.32_</sup>

10. Print out `message` plus three exclamation points as shown in _Snippet 1.33_:

```
>>> message + "!" * 3
'I love Python!!!'
>>>
```

<sup>_Snippet 1.33_</sup>

> We can see the application of a new operation to strings: **`+`** . We use this whenever we want to concatenate (add together) two strings. This only applies to strings, and thus trying to concatenate a string with any other data type will raise an error.
