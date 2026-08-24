<!-- practice -->

# Aim

In this exercise, we will inspect the user-defined module (`musicalnote`) which we created in _Practice Exercise 8.1_ and included as _musicalnote.py_ and compare it with the existing module `random`.

# Steps for Completion

1. Import the `musicalnote` module, as shown in _Snippet 8.23_:

```python
>>> import musicalnote
```

<sup>_Snippet 8.23_</sup>

2. Use the command `dir` on this module, as shown in _Snippet 8.24_:

```python
>>> dir(musicalnote)
```

<sup>_Snippet 8.24_</sup>

The output is as shown in _Snippet 8.25_:

```
['__builtins__', '__cached__', '__doc__', '_file__', '__loader__', '__name__', '__package__', '__spec__', 'listnote']
```

<sup>_Snippet 8.25_<sup>

3. Use the `help` function to understand the module, as shown in _Snippet 8.26_:

```
>>> help(musicalnote)
```

<sup>_Snippet 8.26_<sup>

The output is shown in _Snippet 8.27_:

```
Help on module musicalnote:

NAME
    musicalnote

FUNCTIONS
    listnote()

FILE
    /home/nt-user/workspace/musicalnote.py

(END)
```

<sup>_Snippet 8.27_</sup>

> To exit the `help` menu, press the `q` key.

4. Import the nose module, as shown in _Snippet 8.28_:

```python
>>> import random
```

<sup>_Snippet 8.28_</sup>

5. Use the command `dir` on this module, as shown in _Snippet 8.29_:

```python
>>> dir(random)
```

<sup>_Snippet 8.29_</sup>

The output is as shown in _Snippet 8.30_:

```
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_BuiltinMethodType', '_MethodType', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_inst', '_itertools', '_log', '_pi', '_random', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
```

<sup>_Snippet 8.30_</sup>

6. Use the `help` function to understand the module, as shown in _Snippet 8.31_:

```python
>>> help('random')
```

<sup>_Snippet 8.31_</sup>

The partial output is shown in _Snippet 8.32_:

```
Help on module random:

NAME
    random - Random variable generators.

MODULE REFERENCE
    https://docs.python.org/3.7/library/random

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
        integers
        --------
               uniform within range

        sequences
        ---------
               pick random element
               pick random sample
               pick weighted random sample
               generate random permutation

        distributions on the real line:
        ------------------------------
               uniform
               triangular
               normal (Gaussian)
               lognormal
               negative exponential
               gamma
               beta
               pareto
               Weibull

        distributions on the circle (angles 0 to 2pi)
        ---------------------------------------------
               circular uniform
               von Mises

    General notes on the underlying Mersenne Twister core generator:

    * The period is 2**19937-1.
    * It is one of the most extensively tested generators in existence.
    * The random() method is implemented in C, executes in a single Python step,
      and is, therefore, threadsafe.

CLASSES
    _random.Random(builtins.object)
        Random
            SystemRandom
-- MORE --
```

Thus, using the commands `dir` and `help`, we can conclude that the userdefined module is similar to any module in Python with basic requirements. The commands `dir` and `help` make it easy for us to have a quick glance at its classes, functions, and package content.
