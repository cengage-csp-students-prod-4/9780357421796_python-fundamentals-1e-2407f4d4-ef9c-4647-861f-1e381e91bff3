<!-- practice -->
# Aim

In this exercise, we will practice frozen sets.

# Steps for Completion

1. Go to the _main.py_ file.
2. Create a frozen set as shown in _Snippet 6.130_:

```python
rainbowcolors = frozenset(['V', 'I', 'B', 'G', 'Y', 'O', 'R'])
```

<sup>_Snippet 6.130_</sup>

3. Attempt changing the colors of the rainbow as shown in _Snippet 6.131_:

```
rainbowcolors.add("white")
```

<sup>_Snippet 6.131_</sup>

This will give an error saying that the object does not have the `add` attribute.
