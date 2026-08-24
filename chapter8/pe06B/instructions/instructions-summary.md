<!-- practice -->

# Aim

Suppose you want to remember some dance styles. You will create a text file that has names of `dance_styles` in it, and then read the file using `with` command.

# Steps for Completion

1. Create the _dance_styles.txt_ file using the command shown in _Snippet 8.57_:

```python
>>> f = open('dance_styles.txt', 'w')
```

<sup>_Snippet 8.57_<sup>

2. Write into the file using the commands shown in _Snippet 8.58_:

```python
>>> f.write("Salsa\n")
6
>>> f.write("Jive\n")
5
>>> f.write("Waltz\n")
6
>>> f.write("Latin\n")
6
>>> f.write("Jazz\n")
5
>>> f.write("Contemporary\n")
13
```

<sup>_Snippet 8.59_<sup>

3. Close the file, as shown in _Snippet 8.59_:

```python
>>> f.close()
```

<sup>_Snippet 8.59_</sup>

4. Open the file in read-only mode, as shown in _Snippet 8.60_:

```python
>>> with open("dance_styles.txt", "r") as f:
...     content = f.read()
```

<sup>_Snippet 8.60_</sup>

5. Print the content, as shown in _Snippet 8.61_:

```python
...    print(content)
...
```

<sup>_Snippet 8.61_</sup>

The output will be as shown in _Snippet 8.62_:

```
Salsa
Jive
Waltz
Latin
Jazz
Contemporary
```

<sup>_Snippet 8.62_</sup>
