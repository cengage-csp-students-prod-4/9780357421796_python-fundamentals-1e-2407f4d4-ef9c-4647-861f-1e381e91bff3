<!-- practice -->

# Aim

Suppose you want to add the category of dance style “disco” to your text file from _Practice Exercise 8.6B_ using Python.

# Steps for Completion

1. Open the file in append mode, as shown in _Snippet 8.63_:

```python
>>> f = open('dance_styles.txt', 'a')
```

<sup>_Snippet 8.63_</sup>

The current file content is as shown in _Snippet 8.64_:

```
Salsa
Jive
Waltz
Latin
Jazz
Contemporary
```

<sup>_Snippet 8.64_</sup>

2. Write another dance form to it using the command shown in _Snippet 8.65_:

```
>>> f.write("Disco")
5
```

<sup>_Snippet 8.65_</sup>

3. Close the file as shown in _Snippet 8.66_:

```python
>>> f.close()
```

<sup>_Snippet 8.66_</sup>

4. Read the file. The file content is as shown in _Snippet 8.67_:

```
Salsa
Jive
Waltz
Latin
Jazz
Contemporary
Disco
```

<sup>_Snippet 8.67_</sup>
