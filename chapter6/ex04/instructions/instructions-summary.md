# Scenario

Imagine that you have some data in a list that contains a lot of duplicates that you want to remove, but for simplicity’s sake, you want to avoid writing a `for` loop and building a new list.

# Aim

The aim of this activity is to build a set out of a random set of items. Write a function called **list_to_set** that takes a list and turns it into a set. Do not use a `for` loop or `while` loop to do so.

# Steps for Completion

1. Define the function `list_to_set` to take an argument of a list (`the_list`).
2. Within the `list_to_set` function, use another function to convert the list into a set.
3. Return the set.

_Snippet 6.90_ shows an example of how the function `list_to_set` would work using the correct function:

```python
the_list = [2, 2, 4, 4, 4, 6, 8, 12, 10, 10]
the_set = list_to_set(the_list)
print(the_set)

{2, 4, 6, 8, 10, 12}
```

<sup>_Snippet 6.90_</sup>

> Note: The example above is only showing the logic to what the correct function used within `list_to_set` will do.
