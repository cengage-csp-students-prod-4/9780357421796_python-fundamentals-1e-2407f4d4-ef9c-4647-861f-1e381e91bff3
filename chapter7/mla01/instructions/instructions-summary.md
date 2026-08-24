# Scenario

You have just joined a team of disease researches that are performing disease population simulations. This research team has spent a long time trying to discover new types of cells that can combat the deadly E. coli bacterium. Since the E. coli bacterium is so deadly, the team must use simulations before they can play with the real thing. They have discovered a new type of cell called a Hunter Killer, which me be a very effective destroyer of E. coli cells.

The team is now focused on determining the optimum number of Hunter Killer cells to use to combat a fixed number of E. coli cells in a confined space of a petri dish.

The first major class you need to get familiar with is the `Cell` class. This class is the bare-bones representation of a cell that will be used in the simulation. The focus of this project is to extend the cell base class into different classes and create objects (cells) from these various classes and use them in the simulation.

There are two major classes in this project: `PetriDish` and `Cell`.
You are only required to extend the `Cell` class to create various types of bacteria/organisms in the petri dish. The `PetriDish` class will handle most of the simulation part of the project. You will, however, be required to complete sections in both classes.

Also, each method (activity and task pair) needs to be executed in isolation. As an example, if you want to run `activity2_task1()`, do not run the other methods, such as (`activity1_task1()`) in the same execution of the script. The reason for this is to ensure the randomization is kept the same. Instead, comment out the methods not being executed.

Almost every task requires you to “begin simulation”. This is achieved by the function provided an instance of the `PetriDish` class. Unless explicitly stated, no arguments should be passed into this function.
