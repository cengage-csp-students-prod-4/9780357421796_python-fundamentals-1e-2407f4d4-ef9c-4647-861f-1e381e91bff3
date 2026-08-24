# Creaing lifespans
In this task, for each class, create lifespans for each of the extended classes. This is to be done in a similar way to the implementation in the `Cell` base class.

As can be seen, the base `Cell` class has a lifespan of **100** iterations. Implement the following lifespans:
* `Generic`: 100
* `Ecoli`: 7
* `Structure`: 10000
* `HunterKiller`: 350


Once this is implemented, as usual create a petri-dish of size **30**, and randomly add **10** `Generic`, **20** `Ecoli`, and **30** `HunterKiller` cells to the petri-dish. This is to be done in the order listed above. 

Then use the simulate_n_steps method to step forward 1 step. This is done without providing any argument into the method. Then, for all the cells in the petri-dish, print the lifespan of the cell. Use `activity3_task4()` stub to complete this task.
