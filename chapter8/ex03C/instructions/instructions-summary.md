# Scenario
Build a random number generator using in built Python resources.

# Aim
Write a function called `number_randomizer` whose purpose is to generate random integers between 0 and 100.

The function should use the resources defined in the built-in `random` module. It should take one argument, `num`, which is an integer, and return a list containing `num` random numbers.

For example, calling the function with 6 returns a list of six random numbers as shown in *Snippet 8.38*:
```python
>>> number_randomizer(6)
[21, 63, 89, 57, 40, 74]
```
<sup>*Snippet 8.38*</sup>

# Steps for Completion
1. Import the `random` module.
2. Define a function named `number_randomizer`.
3. Inside the function, use a `for` looping statement and the resources from our imported module to generate random numbers.
4. Using the `number_randomizer` function print the random output numbers for:
	* 2 random numbers
	* 4 random numbers
	* 6 random numbers

Running the script with *python3 main.py* should result in something similar to *Snippet 8.39*:

```
[83, 88]
[82, 80, 44, 13]
[72, 97, 87, 30, 27, 18]
```
<sup>*Snippet 8.39*</sup>

> Please note that your output will differ every time the program is executed.

