<!-- practice -->

# Aim

In this exercise you will use the `try..except` block to handle errors, in this case an `IndexError`.

The simplest way to handle errors is to use the `try…except` block. The code in the `try` section is executed and if an error, which is specified in the `except` block, is thrown, the code in the `except` block is executed.

Once the block finishes executing, the rest of the code executes as well. This prevents errors from causing your program to crash.

# Steps for Completion

1. Create a list of `traffic_signs`, as shown in _Snippet 9.38_:

```python
>>> traffic_signs=["Turn right", "Proceed straight", "Seatbelt required"]
```

<sup>_Snippet 9.38_</sup>

2. Attempt to print the fourth sign, as shown in _Snippet 9.39_:

```python
>>> traffic_signs[3] # IndexError
```

<sup>_Snippet 9.38_</sup>

The exception is shown in _Snippet 9.40_:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

<sup>_Snippet 9.40_</sup>

3. Use a `try..except` block to ensure that the code never reads a value outside the list limits, as shown in _Snippet 9.41_:

```python
>>> try:
...     traffic_signs[4]
... except:
....    print("Error - value exceeds the number inputs")
```

<sup>_Snippet 9.41_</sup>

The output is shown in _Snippet 9.42_:

```
Error - value exceeds the number inputs
```
