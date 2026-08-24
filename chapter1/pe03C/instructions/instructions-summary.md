<!-- practice -->

# Aim

Use the help utility to see the list of keywords.

# Steps for Completion

1. Open the Python interactive shell, you should see the following:

```
Python 3.7.4 (default, Sep  3 2019, 20:41:02)
[GCC 7.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

In the output, you will see a line saying `Type "help", "copyright", "credits" or "license" for more information`.

1. Run `help()` to open the `help` utility.
2. Type `keywords` in the prompt as shown in _Snippet 1.42_:

```
> keywords
```

<sup>_Snippet 1.42_</sup>

You should see the following list as shown in _Snippet 1.43_:

```
Here is a list of the Python keywords.  Enter any keyword to get more help.

False               def                 if                  raise
None                del                 import              return
True                elif                in                  try
and                 else                is                  while
as                  except              lambda              with
assert              finally             nonlocal            yield
break               for                 not
class               from                or
continue            global              pass

>
```

<sup>_Snippet 1.43_</sup>

4. Quit the `help` utility by typing `quit` as shown in _Snippet 1.44_. This should take you back to the interpreter prompt:

```
> quit
```

<sup>_Snippet 1.44_</sup>

> You should not use any word from this list of keywords as an identifier name. Note that you don't have to remember them all as the Python interpreter will restrict you from using them.
