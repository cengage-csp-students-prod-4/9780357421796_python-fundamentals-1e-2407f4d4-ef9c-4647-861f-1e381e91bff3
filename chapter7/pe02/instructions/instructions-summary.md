<!-- practice -->

# Aim

In this exercise, we will add attributes to a `Person` class.

# Steps for Completion

1. First, create the `Person` class with a `name` attribute and instantiate an object without passing any arguments as shown in _Snippet 7.14_:

```
In [1]: class Person:
   ...:     def __init__(self, name):
   ...:         self.name = name
   ...:

In [2]: person1 = Person()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-2-c5f82bb2701d> in <module>
----> 1 person1 = Person()

TypeError: __init__() missing 1 required positional argument: 'name'
```

<sup>_Snippet 7.14_</sup>

Python throws us an error since we need to pass in a `name` argument when instantiating a `Person` object. This argument is passed to the `__init__` method when the object is being instantiated.

2. Instantiate a `Person` object, passing an argument for `name` as shown in _Snippet 7.15_:

```
In [3]: person1 = Person("Bon Clay")
```

<sup>_Snippet 7.15_</sup>

3. Now try to access the attribute from our instance as shown in _Snippet 7.16_:

```
In [4]: person1.name
Out[4]: 'Bon Clay'
```

<sup>_Snippet 7.16_</sup>

4.  Redefine the `Person` class so that it is defining more attributes that instances should be initialized with, for example, name, age, and height in centimeters as shown in _Snippet 7.17_:

```
In [5]: class Person:
   ...:     def __init__(self, name, age, height_in_cm):
   ...:         self.name = name
   ...:         self.age = age
   ...:         self.height_in_cm = height_in_cm
   ...:
```

<sup>_Snippet 7.17_</sup>

5. Now, when instantiating a `Person` object, we'll need to pass in the three arguments: `name`, `age`, and `height_in_cm`. Pass in the three values, as shown in _Snippet 7.18_:

```
In [6]: person1 = Person("Cubert", 62, 180)
In [7]: print(person1.name, person1.age, person1.height_in_cm)
Cubert 62 180
```

<sup>_Snippet 7.18_</sup>
