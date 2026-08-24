<!-- practice -->

# Aim

In this exercise, we will be raising an exception.

# Steps for Completion

1. Create a function `eye_care` to print the medication prescribed, as shown in _Snippet 9.3_:

```python
>>> def eye_care(medication) :
        print(medication)
```

<sup>_Snippet 9.3_</sup>

2. Call the function `eye_care`, as shown in _Snippet 9.4_:

```python
>>> eye_care(Eye)
```

<sup>_Snippet 9.4_</sup>

The exception thrown is shown in _Snippet 9.5_:

```
Traceback (most recent call last):
  File "<stin>", line 1, in <module>
NameError: name 'Eye' is not defined
```

<sup>_Snippet 9.5_</sup>

3. Use can also use the `raise` keyword to raise an exception, as shown in _Snippet 9.6_:

```python
raise NameError('An exception has occurred.')
```

<sup>_Snippet 9.6_</sup>

The exception thrown is shown in _Snippet 9.7_:

```
Traceback (most recent call last):
  File "<stin>", line 1, in <module>
NameError: An exception has occurred.
```

<sup>_Snippet 9.7_</sup>
