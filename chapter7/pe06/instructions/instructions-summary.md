<!-- practice -->

# Aim

In this exercise, we'll define the `Cat` class from which we'll derive our other big cats. The class will have the methods `vocalize` and `print_facts`, and the attributes `mass`, `lifespan`, and `speed`.

The constructor method will take the arguments `mass`, `lifespan`, and `speed` from which it will add the attributes `mass_in_kg`, `lifespan_in_years`, and `speed_in_kph` to the object.

The `vocalize` method will print out `Chuff`, a non-threatening vocalization that's common to several big cats. The `print_facts` method will print out facts about the cat.

# Steps for Completion

1. Define the `Cat` class as shown in _Snippet 7.69_:

```python
class Cat:
	def __init__(self, mass, lifespan, speed):
		self.mass_in_kg = mass
		self.lifespan_in_years = lifespan
		self.speed_in_kph = speed

	def vocalize(self):
		print("Chuff")

	def print_facts(self):
		print(f"The {type(self).__name__.lower()} "f"weighs {self.mass_in_kg}kg," f" has a lifespan of {self.lifespan_in_years} years and " f"can run at a maximum speed of {self.speed_in_kph}kph.")
```

<sup>_Snippet 7.69_</sup>

> The line `type(self).__name__` means that we want the name of the current class of the object, in this case, `Cat` . We then call `str.lower()` on the name in our example.

2. Instantiate a `Cat` object and and call the methods it has as shown in _Snippet 7.70_:

```python
from main import Cat

cat = Cat(4, 18, 48)
cat.vocalize() #Chuff
cat.print_facts() #The cat weighs 4kg, has a lifespan of 18 years and can run at a maximum speed of 48kph.
```

<sup>_Snippet 7.70_</sup>

3. Create the subclasses `Leopard`, `Cheetah`, and `Lion`, which will inherit from the `Cat` class as shown in _Snippet 7.71_:

```python
class Cat:
	def __init__(self, mass, lifespan, speed):
		self.mass_in_kg = mass
		self.lifespan_in_years = lifespan
		self.speed_in_kph = speed

	def vocalize(self):
		print("Chuff")

	def print_facts(self):
		print(f"The {type(self).__name__.lower()} "f"weighs {self.mass_in_kg}kg," f" has a lifespan of {self.lifespan_in_years} years and " f"can run at a maximum speed of {self.speed_in_kph}kph.")
class Cheetah(Cat):
	pass
class Lion(Cat):
	pass
class Leopard(Cat):
	pass
```

<sup>_Snippet 7.71_</sup>

4. Instantiate the new `Leopard`, `Cheetah`, and `Lion` classes as shown _Snippet 7.72_ below.

Despite not adding any methods or attributes to these new classes, if we instantiate them, we'll need to pass in the same arguments that we do when instantiating the `Cat` class. The methods and attributes our instance will have will be identical to a `Cat` class instance:

> Reimport your classes by starting the python interpreter in a new terminal or by restarting the existing python interpreter by entering `quit()`.

```python
from main import Cheetah, Lion, Leopard

cheetah = Cheetah(72, 12, 120)
lion = Lion(190, 14, 80)
leopard = Leopard(90, 17, 58)

cheetah.print_facts()
# The cheetah weighs 72kg, has a lifespan of 12 years and can run at a maximum speed of 120kph.

lion.print_facts()
# The lion weighs 190kg, has a lifespan of 14 years and can run at a maximum speed of 80kph.

leopard.print_facts()
# The leopard weighs 90kg, has a lifespan of 17 years and can run at a maximum speed of 58kph.
```

<sup>_Snippet 7.72_</sup>

As you can see, our subclasses have automatically inherited all of the attributes and methods of the `Cat` class. We have a slight issue on our hands, though.

5. If we call `vocalize` on our instances, they all have the same behavior as shown in _Snippet 7.73_:

```python
cheetah.vocalize()
# Chuff

lion.vocalize()
# Chuff

leopard.vocalize()
# Chuff
```

<sup>_Snippet 7.73_</sup>

In reality, cheetahs make a chirrup, bird-like sound, while lions and leopards roar. We can rectify this by overriding the method in our class. **Overriding** means redefining the implementation of a method defined in a superclass to add or change a subclass's functionality.

6. Override the `vocalize` method for our subclasses as shown in _Snippet 7.74_:

```python
class Cat:
	def __init__(self, mass, lifespan, speed):
		self.mass_in_kg = mass
		self.lifespan_in_years = lifespan
		self.speed_in_kph = speed

	def vocalize(self):
		print("Chuff")

	def print_facts(self):
		print(f"The {type(self).__name__.lower()} "f"weighs {self.mass_in_kg}kg," f" has a lifespan of {self.lifespan_in_years} years and " f"can run at a maximum speed of {self.speed_in_kph}kph.")

class Cheetah(Cat):
	def vocalize(self):
		print("Chirrup")

class Lion(Cat):
	def vocalize(self):
		print("ROAR")

class Leopard(Cat):
	def vocalize(self):
		print("Roar")
```

<sup>_Snippet 7.74_</sup>

7. If we call the `vocalize` method now, we should get different outputs as shown in _Snippet 7.75_:

```python
cheetah.vocalize()
# Chirrup

lion.vocalize()
# ROAR

leopard.vocalize()
# Roar
```

<sup>_Snippet 7.75_</sup>
