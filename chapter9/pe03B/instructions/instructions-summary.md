<!-- practice -->

# Aim

In this exercise we will use a `try…except…else` block to handle a `FileNotFound` error.

The `try…except…else` block is a minor modification of the traditional `try…except` block so that it can include an `else` block. The code in the `else` block is always executed if no error has occurred.

# Steps for Completion

1. Attempt to open a non-existent file in read mode, as shown in _Snippet 9.46_:

```python
f = open("traffic.txt", "r") # FileNotFoundError
print(f.read())
```

<sup>_Snippet 9.46_</sup>

Both commands result in error messages. The error messages are shown in _Snippet 9.47_:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Error 2] No such file or directory: "traffic.txt"
```

<sup>_Snippet 9.47_</sup>

> This needs to be captured in the terminal during runtime.

2. Let’s rewrite those commands in a `try…except…else` block, as shown in _Snippet 9.48_:

```python
try:
	with open('traffic.txt', 'r') as myinputfile:
		for line in myinputfile:
			print(line)
except FileNotFoundError:
	print("File does not exist.")
except ValueError:
	print("A value error occurred")
except Exception:
	print("Something unforeseen happened")
else:
	print("No error occurred opening the file: 'traffic.txt'")

print("Execution will continue to here.")
```

<sup>_Snippet 9.48_</sup>

Run the preceding script; if an error is thrown, the output is shown in _Snippet 9.49_:

```
File does not exist
Execution will continue to here.
```

<sup>_Snippet 9.49_</sup>
