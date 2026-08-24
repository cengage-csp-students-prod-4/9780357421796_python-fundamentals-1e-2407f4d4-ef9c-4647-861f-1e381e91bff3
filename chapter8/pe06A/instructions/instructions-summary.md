<!-- practice -->

# Aim

In this exercise, we will create a file which will contain the natural wonders of the world (New 7 Wonders of Nature).

# Steps for Completion

1. First, we will focus on creating a file. To create a file, head to your terminal and start the Python interpreter.

Use the `open()` method to create a file, and `w+` mode to read a file, as shown in _Snippet 8.51_:

```
>>> f = open('wonders_of_the_world.txt','w+')
```

<sup>_Snippet 8.51_</sup>

You should not see any output after running the preceding command. What it does is simple; it opens a file called _wonders_of_the_world.txt_ in the write mode. Since that file does not exist, a blank file with that name will be created on your filesystem. The `file` object that's created is assigned to the variable `f`, which you can then use to manipulate the file.

2. Write to the file wonders of the world, as shown in _Snippet 8.52_:

```
>>> f.write("Iguazu Falls, Halong Bay, Jeju Island, Puerto Princesa Underground River, Table Mountain, Komodo Island, Amazon Rainforest")
122
```

<sup>_Snippet 8.52_</sup>

3. As a good practice after reading and writing to and from files, close the file as shown in _Snippet 8.53_:

```python
f.close()
```

<sup>_Snippet 8.53_</sup>

4. The output in the text file will be as shown in _Snippet 8.54_:

```
Iguazu Falls, Halong Bay, Jeju Island, Puerto Princesa Underground River, Table Mountain, Komodo Island, Amazon Rainforest
```

<sup>_Snippet 8.54_</sup>

5. Let's add to the list of wonders, reopen the _wonders_of_the_world.txt_ file and add the following list of wonders using the `a+` mode to append new data to the file:

   - The Great Pyramid of Giza
   - Hanging Gardens of Babylon
   - Temple of Artemis
   - Statue of Zeus at Olympia
   - Colossus of Rhodes
   - Ephesus, Mausoleum at Halicarnassus
   - Lighthouse of Alexandria

6. Now close the file. Remember to always do this after you have finished working with a file.

Check the contents of _wonders_of_the_world.txt_; you should see the two strings we wrote:

```
Iguazu Falls, Halong Bay, Jeju Island, Puerto Princesa Underground River, Table Mountain, Komodo Island, Amazon Rainforest

The Great Pyramid of Giza, Hanging Gardens of Babylon, Temple of Artemis, Statue of Zeus at Olympia, Colossus of Rhodes, Ephesus, Mausoleum at Halicarnassus, Lighthouse of Alexandria
```

> If your new content is not a newline, remember that you need to format the string when you write to a file. Try adding a `\n` character to the start or end of a string that you are writing a file.

7. Now, let's read a file. Use the `r` mode to read the file shown in the subsequent code block:

```
>>> f = open('wonders_of_the_world.txt', 'r')
>>> f.read()
Iguazu Falls, Halong Bay, Jeju Island, Puerto Princesa Underground River, Table Mountain, Komodo Island, Amazon Rainforest\n
The Great Pyramid of Giza, Hanging Gardens of Babylon, Temple of Artemis, Statue of Zeus at Olympia, Colossus of Rhodes, Ephesus, Mausoleum at Halicarnassus, Lighthouse of Alexandria\n
```

8. You cannot write in this mode:

```
>>> f.write("Some content")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
io.UnsupportedOperation: not writable
>>> f.close()
```

9. Similarly, you cannot read in write (`w`) or append (`a`) modes:

```
>>> f = open('wonders_of_the_world.txt', 'a')
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
io.UnsupportedOperation: not readable
>>> f.close()
>>> f = open('wonders_of_the_world.txt', 'w')
>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
io.UnsupportedOperation: not readable
>>> f.close()
```

10. If you need to combine both reading and writing, use the `r+` mode:

```
>>> f = open('wonders_of_the_world.txt', 'r+')
>>> f.read()
''
>>> f.write("Great Wall of China")
19
>>> f.close()
```

Note that the `r+` mode appends to the existing file when writing, so it is safe to use on existing files.
