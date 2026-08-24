<!-- practice -->

# Aim

In this exercise you will raise an exception with the `raise` keyword. It is beneficial to use this in a testing environment.

# Steps for Completion

1. Create a list of `traffic_signs`, as shown in _Snippet 9.88_:

```python
>>> traffic_signs = ["Turn right", "Proceed straight", "Seatbelt required"]
```

<sup>_Snippet 9.88_</sup>

2. Print the fourth sign, as shown in _Snippet 9.9_:

```python
>>> val = 3
>>> traffic_signs[val]
```

<sup>_Snippet 9.9_</sup>

The exception thrown is shown in _Snippet 9.10_:

```
Traceback (most recent call last):
  File "<stin>", line 1, in <module>
IndexError: list index out of range
```

<sup>_Snippet 9.10_</sup>

3. To ensure that the code never reads a value outside its limits, we can use the `raise` keyword with an `if` statement, as shown in _Snippet 9.11_:

```python
>>> if val > len(traffic_signs) - 1:
...    raise Exception('Value of val should not exceed size of list {}'.format(val))
```

<sup>_Snippet 9.11_</sup>

The exception thrown is shown in _Snippet 9.12_:

```
Traceback (most recent call last):
  File "main.py", line 5, in <module>
    raise Exception('Value of val should not exceed size of list {}'.format(val))
Exception: Value of val should not exceed size of list 3
```

<sup>_Snippet 9.12_</sup>
