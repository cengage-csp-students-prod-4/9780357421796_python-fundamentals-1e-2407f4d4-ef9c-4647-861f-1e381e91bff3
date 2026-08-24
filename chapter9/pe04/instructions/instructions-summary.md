<!-- practice -->

# Aim

Suppose you create a system in which individuals can book a meeting after 9.00. For simplicity we shall be using a 24 hour clock.

# Steps for Completion

1. Create exception, as shown in _Snippet 9.56_:

```python
class TimeEnteredNotValidError(Exception):
    def __init__(self):
        self.message = "The time is not valid"
```

<sup>_Snippet 9.56_</sup>

2. Suppose the `time_entered` is **8**, as shown in _Snippet 9.57_:

```python
time_entered = 8
```

<sup>_Snippet 9.57_</sup>

3. Use a `try…catch` block to raise the exception:

```python
try:
    if time_entered < 9:
        raise TimeEnteredNotValidError
except TimeEnteredNotValidError as e:
    print(e.message)
```

<sup>_Snippet 9.58_</sup>

The output is shown in _Snippet 9.59_:

```
The time is not valid
```

<sup>_Snippet 9.59_</sup>
