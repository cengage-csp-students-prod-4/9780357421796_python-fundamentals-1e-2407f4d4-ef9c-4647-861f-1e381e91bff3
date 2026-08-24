# Best Practices to Follow:
* Write detailed comments and doc-string.
* Organize and structure code for readability.
* Write your own test cases to check correctness.


# Setting up the Petri dish

## Activity 1: 
Your first objective is to familiarize yourself with the `PetriDish` class.

### Creating different petri dishes.
The `PetriDish` class takes a single argument (size) when creating petri dish objects. Create a petri dish of size 5 for task 1 using the `activity1_task1()` stub, and execute the `begin_simulation()` method of the newly created `PetriDish` object. Don't forget to run the simulation to see the output.

### Place cells into the petri dish.
 Take the time now to have a look at the `Cell` class. It's the basic structure of a cell, and has no distinguishing features other than the symbol c, which is used to distinguish this base class cell from other cells (which will come later). 

For now, we can place this cell into the petri dish. 
In order to be able to complete this task you need to complete the `add_to_world` method in the `PetriDish` class. The class takes in a `cell` object as input and does three things. 
Firstly, it should be noted that the `PetriDish` class contains a dictionary called `self.world`, which is a mapping of a petri dish coordinate to a symbol of cell occupying that space. Use the x,y coordinate information in the cell to populate the petri dish map with the symbol of the cell. 
Secondly, the `PetriDish` also has a list of cells called `self.all_cells`, which it uses to keep track of all the alive cells. The new cell needs to be added to this list. 
Finally, as a preventative measure, the petri dish needs to keep track of all the free positions on the petri-dish. This is done via the `self.available_positions` list. This list contains a list of all the positions that are currently free. Obviously, when the petri-dish is created, this is completely full, with all the possible positions the petri-dish can take. As cells are added, the position the cell is in needs to be removed from the list. It also makes sense to check if the position is available before adding the cell to the petri-dish. 

All of these things must be done in this method. Once all of these things are done create a petri-dish of size **30** and add **4** cells at positions **(0,0)**, **(5,5)**, **(10,10)**, and **(15,15)**, and begin the simulation. Use `activity1_task2()` stub to complete the task. 

To begin the simulation just print what the petri-dishes look like with the cells in them.


