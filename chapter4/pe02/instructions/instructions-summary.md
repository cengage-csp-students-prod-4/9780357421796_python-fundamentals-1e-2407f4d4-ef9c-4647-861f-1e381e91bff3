<!-- practice -->
# Aim

Define global and local variables. We will also demonstrate the difference between global and local variables.

# Steps for Completion

1. First, declare and initialize `number` to **5** as shown in _Snippet 4.6_:

```python
number = 5
```

<sup>_Snippet 4.6_</sup>

2. Then, define a function called `summation` that takes two named parameters `first` and `second` as shown in _Snippet 4.7_:

```python
def summation(first, second):
```

<sup>_Snippet 4.7_</sup>

3. Inside of the function, add up the two parameters that were passed in and the global variable number as shown in _Snippet 4.8_:

```python
	total = first + second + number
```

<sup>_Snippet 4.8_<sup>

4. Return the final total as shown in _Snippet 4.9_:

```python
	return total
```

<sup>_Snippet 4.9_</sup>

5. Call the `summation` function with two parameters, as expected (`10` and `20`) as shown in _Snippet 4.10_:

```python
summation(10, 20)
```

<sup>_Snippet 4.10_</sup>

6. Print out the initial value of the number as shown in _Snippet 4.11_:

```python
print("The first number we initialized was " + str(number))
```

<sup>_Snippet 4.11_</sup>

7. Try to access the local variable total as shown in _Snippet 4.12_:

```python
print("The total after summation is " + str(total))
```

<sup>_Snippet 4.11_</sup>

Note the use of the built-in function, `str()`, which returns the string version of an object.

The final code should resemble _Snippet 4.13_ shown below:

```python
# Initialize global variable "number" to 5
In [1]: number = 5
"""
Define function "summation" that takes two parameters
Note that the function accesses the global variable "number"
"""
In [2]: def summation(first, second):
   ...:     # Add the parameters and global number together
   ...:     total = first + second + number
   ...:     # Return result
   ...:     return total
   ...:

In [3]: summation(10, 20)
Out[3]: 35

# Print out the initial value of "number"
In [4]: print("The first number we initialized was " + str(number))
The first number we initialized was 5

# Try to access the local variable "total"
In [5]: print("The total after summation is " + str(total))
```

<sup>_Snippet 4.13_</sup>

Running this code will produce the output shown in _Snippet 4.14_ below:

```
NameError                                 Traceback (most recent call last)
<ipython-input-5-f97c51e0e982> in <module>
----> 1 print("The total after summation is " + str(total))

NameError: name 'total' is not defined
```

<sup>_Snippet 4.14_</sup>

As you can see, this results in an error, because we are trying to access the local variable `total` from the global scope. This is just to demonstrate that we cannot access local variables globally.

9. Now, change the code shown in _Snippet 4.15_; we will get different output upon calling the function:

```python
# Initialize global variable "number" to 5
In [1]: number = 5
"""
Define function "summation" that takes two parameters
Note that the function accesses the global variable "number"
"""
In [2]: def summation(first, second):
   ...:     # Add the parameters and global number together
   ...:     total = first + second + number
   ...:     # Return result
   ...:     return total
   ...:

# Call the "summation" function with two parameters as excepted
# Assign the result of "summation" to the variable "outer_total
In [3]: outer_total = summation(10, 20)

# Print out the initial value of "number"
In [4]: print("The first number we initialized was " + str(number))
The first number we initialized was 5

# Try to access the local variable "total"
In [5]: print("The total after summation is " + str(outer_total))
The total after summation is 35
```

<sup>_Snippet 4.15_</sup>

Notice that we are now assigning the result of the `summation` function to the `outer_total` variable.

The output now changes to what we expect, without errors, and it looks like _Snippet 4.16_:

```
The first number we initialized was 5
...
The total after summation is 35
```

<sup>_Snippet 4.16_</sup>
