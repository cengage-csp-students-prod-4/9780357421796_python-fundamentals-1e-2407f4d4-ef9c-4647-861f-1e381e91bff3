# Aim

We will create a dictionary and verify its type.

# Steps for Completion

1. Go to the _main.py_ file.

2. Use the `dict` function or curly bracket notation to create a dictionary and assign it to a variable, **location**.

3. Within a `print` function, use the built-in `type` function on `location` to see if it is an instance of the `dict` class.

A typical example of a dictionary is shown in _Snippet 6.5_:

```python
location = dict(
	state="CA",
	city="Los Angeles"
)
```

<sup>_Snippet 6.5_</sup>

In this example, `state` and `city` are **keys**, while `CA` and `Los Angeles` are the respective **values** assigned to them.
