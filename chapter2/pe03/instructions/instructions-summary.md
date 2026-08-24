<!-- practice -->

# Aim

See how list references work:

# Steps for Completion

1. Create a new list, as shown in _Snippet 2.71_:

```
>>> list_1 = [1, 2, 3]
```

<sup>_Snippet 2.71_</sup>

2. Then, assign a new variable, `list_2`, to `list_1` using the command shown in _Snippet 2.72_:

```
>>> list_2 = list_1
```

<sup>_Snippet 2.72_</sup>

3. Any changes that we make to `list_2` will be applied to `list_1`. Append **4** to `list_2` and check the contents of `list_1` as shown in _Snippet 2.73_:

```
>>> list_2.append(4)
>>> list_1
[1, 2, 3, 4]
```

<sup>_Snippet 2.73_</sup>

4. Any changes that we make to `list_1` will be applied to `list_2`. Insert the value **a** at index `0` of `list_1`, and check the contents of `list_2` as shown in _Snippet 2.74_:

```
>>> list_1[0] = "a"
>>> list_2
['a', 2, 3, 4]
>>>
```

<sup>_Snippet 2.74_</sup>

This is because both variables reference the same object.

> We will be covering lists in further depth in future lessons.
