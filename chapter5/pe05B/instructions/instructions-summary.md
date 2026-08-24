<!-- practice -->

# Aim

In this exercise, we will take a look at some practical examples of slicing. Consider a tuple of numbers from one through ten as shown in _Snippet 5.28_:

```python
numbers = tuple(range(1,11))
print(numbers)

(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
```

<sup>_Snippet 5.28_</sup>

# Steps for Completion

We will create a list using list comprehensions and cast it to a tuple by using the `tuple()` method.

To demonstrate tuple slicing, we will to do two things:

• Create a new tuple containing only the even numbers in the tuple

• Create a new tuple containing only the odd numbers in the tuple

1. To slice the tuple so that we have only the even numbers, start at the second index and finish at the end, while skipping one place every step.

In code, that looks something like that shown in _Snippet 5.29_:

```python
numbers = tuple([i for i in range(1,11)])
print(numbers)

even = numbers[1::2]
print(even)

(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
(2, 4, 6, 8, 10)
```

<sup>_Snippet 5.29_</sup>

For this operation, we set the start index to **1** (the second element of the tuple) and the increment to **2**, so that it skips one element every time.

2. To slice the tuple so that we have only the odd numbers, start at the beginning of the tuple and finish at the end, while skipping one place every step.

In code, that looks like that shown in _Snippet 5.30_:

```python
numbers = tuple([i for i in range(1,11)])
odd = numbers[::2]
print(odd)

(1, 3, 5, 7, 9)
```

<sup>_Snippet 5.30_</sup>

For this operation, we start at index zero (the first element of the tuple) and set the increment to **2**, so that it skips one element every time.
