<!-- practice -->

# Aim

In this exercise, we will practice different ways of importing modules and module objects.

> The `calculator` module has been provided to you.

There are several ways we can import and use the resources defined in a module. You have already seen one way to go about importing modules, which is importing the whole module by using the `import` keyword and then calling a resource inside it by using the dot (`.`) notation, shown in _Snippet 8.13a_ below:

```
>>> import calculator
>>> calculator.add(8, 9)
17
```

<sup>_Snippet 8.13a_</sup>

Another way of accessing a module's resources is to use the `from…import…` syntax, shown in _Snippet 8.13b_:

```
>>> from calculator import *
>>> add(8, 9)
17
```

<sup>_Snippet 8.13b_</sup>

Note that the `*` in the preceding example tells Python to import everything in the module named `calculator`. We can then use any resource defined in the `calculator` module by referring to the resource name (in our case, the `add` function) directly. You should note that using `*` is not a good practice. You should always strive to import exactly what you need.

What if you want to only import a few resources from the module? In that case, you can name them directly, as shown in _Snippet 8.14a_ below:

```
>>> from calculator import add
>>> add(8, 9)
17
```

<sup>_Snippet 8.14a_</sup>

Another useful thing you can do is name your imports by using the `as` keyword shown in _Snippet 8.14b_:

```
>>> from calculator import add as a
>>> a(8, 9)
17
>>> import calculator as calc
>>> calc.add(8,9)
17
```

<sup>_Snippet 8.14b_</sup>

This can come in handy when you have a module or resource with a long name that you will be referring to in many places.

You can also group many imports by using brackets for easier readability shown in _Snippet 8.14c_:

```
>>> from random import (choice, choices)
```

<sup>_Snippet 8.14c_</sup>
