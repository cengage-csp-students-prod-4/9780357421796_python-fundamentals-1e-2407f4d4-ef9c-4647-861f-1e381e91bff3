# Scenario

You are completing some code, but you have an unhandled error. What do you do to make sure that the error doesn't stop your program prematurely?

# Aim

In this activity, we will practice handling errors. The code in _Snippet 9.53_ throws an error.

The following code throws an error:

```python
import random

print(random.randinteger(5,15))
```

<sup>_Snippet 9.53_</sup>

Identify and handle the error so that when it occurs, the message is printed to the terminal.

# Steps for Completion

1. Go to your _main.py_ file.

2. Take the code block from _Snippet 9.53_, and amend to it so that it catches the error, using a `try… except` block.

3. Within the `try... except` block make the exception look for an `AttriubuteError` and print **Double check the attributes in your code and try again.**
