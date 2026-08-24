# Extending base classes 
In particular, you will extend the Cell base class to create specialized variants of the Cell class. In this activity, all you will modify is the symbol for your class extensions, but in later activities, the distinguishing features of each cell type will become larger. This should be done by overriding the `_set_symbol_()` method.

> In the `__init__` function for the extended class, use the `__init__`of the base class using the `super()` method.

# `Generic` cell class
In this task, you need to create a new class called the `Generic` cell class, which extends the `Cell` base class. The `Generic` cell class needs to have the symbol **o**. All other properties that are inherited from the `Cell` class are to remain the same for this activity.
Once this is done, create a petri-dish of size **30** and, like before, create **10** instances of this `Generic` cell type with randomly allocated positions. Use `activity2_task1()` stub to complete this task.

Once this is done, begin the simulation!

