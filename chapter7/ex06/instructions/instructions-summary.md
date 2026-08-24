# Scenario
Suppose you work for a wildlife conservation organization. You are working on creating a system to educate the general public about different animals and get them more interested in conservation.

# Aim
Create a `Eagle` class that inherits from the `Bird` class and has a clutch size (eggs laid in one nesting) attribute. Change the behavior of instances of the `Eagle` class to include this clutch size fact when they're printed.

# Steps for Completion

1. Go to your *main.py* file.

2. Define the `Eagle` class that inherits from the `Bird` class. Override the `__init__` initializer method and add a `clutch_size` attribute with the value of **3**.

3. Override the `__str__` method and modify it to include mention of the clutch size.

4. At the bottom of the script we have initialized an instance of the `Eagle` class and called `print` on the instance, which should display facts about the eagle.

Run the script by using *python3 main.py* in the terminal. The output should be as shown in *Snippet 7.86*:

```
The eagle has a wingspan up to 7.5ft, has a lifespan of 20 years and can fly at a maximum speed of 99mph. It also has a clutch size up to 3.
```
<sup>*Snippet 7.86*</sup>

