To generate a `KeyError`:

1. Create the dictionary shown in _Snippet 9.29_:

```python
dinning = dict (
    name = "Johnny's Restaurant",
    location = "Times Square"
)
```

<sup>_Snippet 9.29_</sup>

2. Write a `print` statement that uses a key that’s not defined in this dictionary.

Running the script with _python3 main.py_ should result in only one console error similar to the example below:

```
KeyError: 'address'
```
