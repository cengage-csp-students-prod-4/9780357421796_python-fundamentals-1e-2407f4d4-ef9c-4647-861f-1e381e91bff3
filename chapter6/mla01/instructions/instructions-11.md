# Update the `populate_galaxy_map()` function

Next, we will be updating the `populate_galaxy_map()` function. The next task is to keep track of the data given to you by the `generate_object()` function, which will include information about the distance, the coordinates, and the symbol used to represent the object. The list should store the encountered objects as tuples in the form of (distance, coordinates, symbol).

Ensure that the list returned by the `populate_galaxy_map()` function is sorted by distance in ascending order.

The last step in completing the populate_galaxy_map() function is to continue to receive object information from the `generate_object()` function. Each object received needs to be added to the objects_encountered list, and the galaxy map needs to be updated accordingly. Keep doing this until you encounter a symbol of **‘G’** (which is the goal). At this point, break from the loop and return the sorted list of objects encountered so far.
