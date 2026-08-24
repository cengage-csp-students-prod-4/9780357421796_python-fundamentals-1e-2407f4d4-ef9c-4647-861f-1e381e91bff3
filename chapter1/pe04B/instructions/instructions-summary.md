<!-- practice -->

# Aim

Take a look at the importance of proper indentation.

# Steps for Completion

1. Open your interpreter and type the statement shown in _Snippet 1.66_:

```
>>> if True:
```

<sup>_Snippet 1.66_</sup>

2. Press the **Shift** + **Enter** keys to create a new line. The interpreter will show three dots `…` in place of the usual `>>>` prompt, which means you're on another line. Type four spaces and then write your statement as shown in _Snippet 1.67_:

```
>>> if True:
...    print(1)
```

<sup>_Snippet 1.67_</sup>

3. Then type our last statement with an unequal number of spaces. This should raise an error when we execute it. Create another new line, type three spaces, and write the final statement as shown in _Snippet 1.68_. Then, press the **Enter** key to execute the whole snippet:

```
>>> if True:
... 	print(1)
...  print(2)
```

<sup>_Snippet 1.68_</sup>

Executing this should raise the indentation error shown in _Snippet 1.69_:

```
File "<stdin>", line 3
	print(2)
				 ^
IndentationError: unindent does not match any outer indentation level
```

<sup>_Snippet 1.69_</sup>

4. This error tells us that the indentation for our last line, which was three spaces, didn't match our first line's indentation, which was four spaces. Indentation for statements in a block is dictated by the first statement's indentation level. To fix this, indent that line in the same way as the first as shown in _Snippet 1.70_, and it should run normally now:

```
>>> if True:
...     print(1)
...     print(2)
...
1
2
>>>
```

<sup>_Snippet 1.70_</sup>

> While you can use any number of spaces to indent a statment, the general convention is to use four spaces.
