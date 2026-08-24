<!--practice -->

# Aim

In this exercise, you will see how to use indexing to access tuples:

# Steps for Completion

1. Create a new `pets` tuple with the elements `dog`, `cat`, and `parrot` as shown in _Snippet 5.22_:

```python
pets = ('dog','cat','parrot')
```

<sup>_Snippet 5.22_</sup>

2. Print `pets[1]` to access the second index as shown in _Snippet 5.23_:

```python
print(pets[1])
```

```
'cat'
```

<sup>_Snippet 5.23_</sup>

3. Try to print an index that is not in the tuple. Python will raise an `IndexError`, as shown in _Snippet 5.24_:

```python
print(pets[3])
```

```
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    print(pets[3])
IndexError: tuple index out of range
```

<sup>_Snippet 5.24_</sup>

4. Indices can also be negative. If you use a negative index, `-1` will reference the last element in the tuple, `-2` will refer to the second from last element in the tuple, and so on. Use the code shown in _Snippet 5.25_ to access the tuple:

```python
pets = 'dog', 'cat', 'parrot', 'gerbil'

print(pets[-1])

print(pets[-2])

print(pets[-3])
```

```
'gerbil'
'parrot'
'cat'
```

<sup>_Snippet 5.25_</sup>

5. As with list indices, tuple indices must always be integers, and trying to use other types will result in a `TypeError`, as shown in _Snippet 5.26a_ and _Snippet 5.26b_. Type a string and a float value as an index:

```python
pets = 'dog', 'cat', 'parrot'
pets['1']
```

```
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    pets['1']
TypeError: tuple indices must be integers or slices, not str
```

<sup>_Snippet 5.26a_</sup>

```python
pets[1.5]
```

```
Traceback (most recent call last):
  File "main.py", line 3, in <module>
    pets[1.5]
TypeError: tuple indices must be integers or slices, not float
```

<sup>_Snippet 5.26b_</sup>

The error message presented here mentions `slices`, and you might be wondering what slices are. This brings us to the alternative way in which you can access tuple elements: slicing.
