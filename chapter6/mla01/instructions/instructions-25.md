## Make it your own

Determine whether there is enough fuel to reach the goal, assuming the spacecraft can initially cover a distance of 50 units, and every subsequent **‘F’** object encountered increases the amount of fuel by 15 units.

Instead of the simple distance-from-origin measure that we have implemented, implement a measure of the distance from each object to every other object. Then, implement greedy pathfinding to establish the best path to the goal and the total distance covered.

Similar to the preceding extension, implement the A\* search, using the Manhattan distance as a heuristic.

The Manhattan distance is given by the following formula: _distance(x,y) = abs(x + y)_. One way to imagine this distance calculation is to imagine that only horizontal and vertical movements are allowed, and the cost/distance travelled with each movement is 1 unit. Therefore, to go to a position that is diagonally 1 square away, you would need to travel 1 unit horizontally and another vertically, making the Manhattan distance for those two points 2.

As an extra challenge, iterate through the different randomized seeds until you find maps that have a valid solution, where the spacecraft has enough fuel to reach the goal.
