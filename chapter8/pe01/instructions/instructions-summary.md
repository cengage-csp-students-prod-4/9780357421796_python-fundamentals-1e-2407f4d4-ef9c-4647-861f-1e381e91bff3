<!-- practice -->

# Aim

In this exercise, we are creating a user-defined module which will print the different musical note lengths.

# Steps for Completion

> To create a module, first check if the module already exists. If it exists, then create the module with a different name.

1. Import the `musicalnote` module, as shown in _Snippet 8.3_:

```python
>>> import musicalnote
```

<sup>_Snippet 8.3_</sup>

The error message is shown in _Snippet 8.4_:

```
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'musicalnote'
```

<sup>_Snippet 8.4_</sup>

The module does not exist; now create a module with the name `musicalnote`.

2. Create a file `musicalnote.py` that prints the different lengths of musical notes. The file is shown in _Snippet 8.5_:

```python
def listnote():
    print("Whole note, Half note, Quarter note, Eighth note, and Sixteenth note")
```

<sup>_Snippet 8.5_</sup>

3. Import the module and print the values as shown in _Snippet 8.6_:

```python
>>> import musicalnote
>>> musicalnote.listnote()
```

<sup>_Snippet 8.6_</sup>

The output is as shown in _Snippet 8.7_:

```
Whole note, Half note, Quarter note, Eighth note, and Sixteenth note
```

<sup>_Snippet 8.7_</sup>

We have successfully created a new module `musicalnote` which prints the name of the musical notes.
