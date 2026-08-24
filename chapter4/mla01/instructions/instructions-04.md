## Make it your own

As the algorithm performs division of numbers with high precision, it is very common to see really big numbers after the period (for example: 1200.2300001), which is not desirable because of several reasons:

1. may cause confusion to some users when they see such big numbers;
2. uses more memory to store a bigger number;
3. it just does not make sense to display currency number in this format.

For this reason, you are going to implement a utility function to format any number into the appropriate currency format, using 2 decimal places.

For example:
The number 1200.2300001 would be became: 1200.23

> Take a look at the formatting options for python native.
