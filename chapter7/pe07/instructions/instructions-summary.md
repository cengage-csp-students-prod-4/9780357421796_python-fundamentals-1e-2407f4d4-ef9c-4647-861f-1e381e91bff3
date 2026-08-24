<!-- practice -->

# Aim

In the real world, lions and tigers can naturally mate to create a hybrid known as a liger or a tigon. Ligers are much larger than either lions or tigers, they are social like lions, have stripes, and, just like tigers, they like swimming. We're going to create a `Liger` class that inherits from both the `Lion` and `Tiger` class we're going to define.

In this exercise, we will learn how to implement multiple inheritance.

# Steps for Completion

1. Define the `Lion` and `Tiger` classes. For simplicity, we'll hardcode the `mass`, `lifespan`, and `speed` attributes. They'll both inherit from the `Cat` class as shown in _Snippet 7.88_:

```python
class Cat:
    def __init__(self, mass, lifespan, speed):
        self.mass_in_kg = mass
        self.lifespan_in_years = lifespan
        self.speed_in_kph = speed

    def vocalize(self):
        print("Chuff")

    def __str__(self):
        return f"The {type(self).__name__.lower()} "\
            f"weighs {self.mass_in_kg}kg,"\
            f" has a lifespan of {self.lifespan_in_years} years and "\
            f"can run at a maximum speed of {self.speed_in_kph}kph."

class Lion(Cat):
    def __init__(self, mass=190, lifespan=14, speed=80):
        super().__init__(mass, lifespan, speed)
        self.is_social = True

    def vocalize(self):
        print("ROAR")

class Tiger(Cat):
    def __init__(self, mass=310, lifespan=26, speed=65):
        super().__init__(mass, lifespan, speed)
        self.coat_pattern = "striped"

    def swim(self):
        print("Splash splash")

    def vocalize(self):
        print("ROAR")
```

<sup>_Snippet 7.88_</sup>

2. Then, define the `Liger` class, which will inherit from both the `Tiger` and `Lion` classes as shown in _Snippet 7.89_:

```python
class Liger(Lion, Tiger):
	pass
```

<sup>_Snippet 7.89_</sup>

3. On testing it out, we should see that the `Liger` class has inherited attribute from both the `Lion` and `Tiger` classes. The `Liger` class has both the `coat_pattern` attribute and `swim()` method of the `Tiger` class and the `is_social` attribute of the `Lion` class as seen in _Snippet 7.90_:

```
>>> from main import Liger
>>> liger = Liger()
>>> liger.swim()
Splash splash
>>> liger.is_social
True
>>> liger.coat_pattern
'striped'
>>>
```

<sup>_Snippet 7.90_</sup>
