## Make it your own

Extend the petri-dish project to include a new type of object defined by the virus class. Make several types of virus, each with their own set of rules to compete with the bacterial cells in the original project. Some suggestions for effects include:

- Chess knight-like movement
- Poisoning ability, which causes death on the target in 5 turns from being poisoned.
- Vampirism (random chance any virus is spawned with vampirism (1%), and life of that particular virus particle is increased to 1,000 turns, and each neighboring cell has a 50% chance of being converted into a vampire).
- Paired cells. Create a new type of bacterium that requires one Male and one Female cell type to be next to each other in order to reproduce.
- Create a kill switch/key-press that instantly kills 50% of the living things in the petri-dish.
- Modify the `HunterKiller` class such that each `HunterKiller` cell keeps track of its own kill count, and replicates when it has killed 100 `Ecoli` cells.
