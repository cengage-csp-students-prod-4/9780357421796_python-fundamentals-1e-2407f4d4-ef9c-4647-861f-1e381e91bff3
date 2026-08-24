# Create methods for handling static methods and static variables
The scientists at the facility want to be able to extract statistics on the number of cells created. 

In this activity, you need to create methods for handling static methods and static variables. Essentially, these are variables and methods that apply to the class rather than the object.

## Incrementing the cell counts
Ensure that each newly instantiated cell of the extended `Cell` class increments the count of that class. For example, each time an `Ecoli` cell is created, the count needs to increment. This needs to be done for each class rather than just for `Cell`, (you cannot just inherit the number from the `Cell` class. This is because the scientists want to be able to know how many E. coli cells are created). 
Once this is done, create a petri-dish of size **30**. 

Randomly add **10** `Generic`, **20** `Ecoli`, and **30** `HunterKiller` cells to the petri-dish. The order of creation is not important. 

When you print the result, you should get `Cell` count of **60**, **10** `Generic`, **20** `Ecoli`, **0** `Structure`, **30** `HunterKiller`.
Use `activity3_task1()` stub to complete this task.
