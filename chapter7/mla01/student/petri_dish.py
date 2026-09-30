#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Petri dish disease-population simulation.

Cell is the base class; Generic, Ecoli, Structure and HunterKiller extend it
by overriding the symbol, lifespan and movement hooks that Cell.__init__ and
PetriDish.tick() call polymorphically. Each class keeps its own class-level
`count` so the researchers can see how many of each type exist.
"""

from random import choice, seed
from itertools import product
from time import sleep
import subprocess as sp


SEED_NUMBER = 0

seed(SEED_NUMBER)

empty_cell = ' '

replication_cells = ['up', 'right', 'down', 'left']

replication_order = {
    'up': (-1, 0),
    'right': (0, 1),
    'down': (1, 0),
    'left': (0, -1)
}


class Cell:
    """Bare-bones cell. Subclasses override the _set_* hooks and movement."""
    count = 0

    def __init__(self, position=(0, 0)):
        self.x = position[0]
        self.y = position[1]
        self.lifespan = self._set_lifespan()
        self.symbol = self._set_symbol()
        Cell.count += 1

    def __repr__(self):
        return self.symbol

    def _set_symbol(self):
        return 'c'

    def _set_lifespan(self):
        return 100

    def get_location(self):
        return f'(x={self.x}, y={self.y})'

    def intended_position(self):
        return (self.x, self.y)

    def set_location(self, position):
        self.x, self.y = position

    @staticmethod
    def reduce_count():
        Cell.count -= 1

    @staticmethod
    def reset_count():
        Cell.count = 0


class Generic(Cell):
    """Wandering cell: symbol 'o', lifespan 100, moves up to 2 squares per axis."""
    count = 0  # own counter; without this, Generic.count would read Cell.count

    def __init__(self, position=(0, 0)):
        super().__init__(position)   # sets x, y, symbol, lifespan; Cell.count += 1
        Generic.count += 1           # name the class explicitly, NOT self.count

    def _set_symbol(self):
        return 'o'

    def _set_lifespan(self):
        return 100

    def intended_position(self):
        """Current position plus a random offset in [-2, 2] on each axis."""
        moves = list(range(-2, 3))   # [-2, -1, 0, 1, 2]
        return (self.x + choice(moves), self.y + choice(moves))

    @staticmethod
    def reduce_count():
        """Decrement this class's count and the base Cell total."""
        Generic.count -= 1
        Cell.reduce_count()

    @staticmethod
    def reset_count():
        """Reset only this class's count (Cell is reset separately)."""
        Generic.count = 0


class Ecoli(Cell):
    """E. coli: symbol 'e', lifespan 7, stationary (replication handled in tick)."""
    count = 0

    def __init__(self, position=(0, 0)):
        super().__init__(position)
        Ecoli.count += 1

    def _set_symbol(self):
        return 'e'

    def _set_lifespan(self):
        return 7

    # intended_position() is inherited from Cell -> does not move

    @staticmethod
    def reduce_count():
        Ecoli.count -= 1
        Cell.reduce_count()

    @staticmethod
    def reset_count():
        Ecoli.count = 0


class Structure(Cell):
    """Static obstacle: symbol 'S', lifespan 10000, never moves."""
    count = 0

    def __init__(self, position=(0, 0)):
        super().__init__(position)
        Structure.count += 1

    def _set_symbol(self):
        return 'S'

    def _set_lifespan(self):
        return 10000

    @staticmethod
    def reduce_count():
        Structure.count -= 1
        Cell.reduce_count()

    @staticmethod
    def reset_count():
        Structure.count = 0


class HunterKiller(Cell):
    """E. coli hunter: symbol 'x', lifespan 350, moves up to 1 square per axis."""
    count = 0
    kill_count = 0

    def __init__(self, position=(0, 0)):
        super().__init__(position)
        HunterKiller.count += 1

    def _set_symbol(self):
        return 'x'

    def _set_lifespan(self):
        return 350

    def intended_position(self):
        """Current position plus a random offset in [-1, 1] on each axis."""
        moves = [-1, 0, 1]
        return (self.x + choice(moves), self.y + choice(moves))

    @staticmethod
    def reduce_count():
        HunterKiller.count -= 1
        Cell.reduce_count()

    @staticmethod
    def reset_count():
        HunterKiller.count = 0


# ---------------------------------------------------------------------------
# Task 14 ("make it your own"): a Virus family with knight-style movement.
# ---------------------------------------------------------------------------

class Virus(Cell):
    """Base class for viruses. Tracks its own total across all virus types."""
    count = 0

    def __init__(self, position=(0, 0)):
        super().__init__(position)
        Virus.count += 1

    def _set_symbol(self):
        return 'v'

    def _set_lifespan(self):
        return 50

    @staticmethod
    def reduce_count():
        Virus.count -= 1
        Cell.reduce_count()

    @staticmethod
    def reset_count():
        Virus.count = 0


class KnightVirus(Virus):
    """Virus that moves like a chess knight: 2 squares one way, 1 the other."""
    count = 0
    KNIGHT_MOVES = [(1, 2), (2, 1), (2, -1), (1, -2),
                    (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

    def __init__(self, position=(0, 0)):
        super().__init__(position)   # Virus.count and Cell.count both increment
        KnightVirus.count += 1

    def _set_symbol(self):
        return 'k'

    def intended_position(self):
        dx, dy = choice(KnightVirus.KNIGHT_MOVES)
        return (self.x + dx, self.y + dy)

    @staticmethod
    def reduce_count():
        KnightVirus.count -= 1
        Virus.reduce_count()         # cascades up: Virus -> Cell

    @staticmethod
    def reset_count():
        KnightVirus.count = 0


def reset_all_cell_counts():
    """Reset the class-level count of every cell type to 0."""
    cell_types = [Cell, Generic, Ecoli, Structure, HunterKiller, Virus, KnightVirus]
    for cell_type in cell_types:
        cell_type.reset_count()
    HunterKiller.kill_count = 0


class PetriDish:
    def __init__(self, size=30):
        self.SIZE = size
        self.all_positions = []
        self.available_positions = []
        self.world = self._create_world()
        self.counter = 0
        self.world_state = ['']
        self.all_cells = []
        for i in range(self.SIZE):
            new_col = dict()
            for j in range(self.SIZE):
                new_col[j] = empty_cell
            self.world[i] = new_col

    def __repr__(self):
        return_string = '|'
        return_string += '-' * self.SIZE
        return_string += '|\n|'
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                return_string += self.world[(i, j)]
            return_string += '|\n|'
        return_string += '-' * self.SIZE
        return_string += '|'
        return return_string

    def _create_world(self):
        world = dict()
        self.all_positions = [(i, j) for i, j in product(range(self.SIZE), range(self.SIZE))]
        for position in self.all_positions:
            world[position] = empty_cell
            self.available_positions.append(position)
        return world

    def add_to_world(self, cell):
        """
        Place a cell in the dish if its position is free.

        Keeps the three views of the world in sync:
          1. self.world maps the position to the cell's symbol
          2. self.all_cells gains the cell
          3. self.available_positions loses the position
        Returns True if the cell was placed, False if the square was taken
        or off the dish.
        """
        position = (cell.x, cell.y)
        if position not in self.available_positions:
            return False
        self.world[position] = cell.symbol
        self.all_cells.append(cell)
        self.available_positions.remove(position)
        return True

    def _has_world_changed(self):
        start = self.world_state[-1]
        end = self.__repr__()
        return start != end

    def update_world(self):
        for key in self.world:
            self.world[key] = ' '
        for cell in self.all_cells:
            self.world[(cell.x, cell.y)] = cell.symbol

    def print_header(self):
        sp.call('clear', shell=True);
        print(f'Iteration: {self.counter} | ', end='')
        print(f'Total Cells: {Cell.count} | ', end='')
        print(f'Generic Cells: {Generic.count} | ', end='')
        print(f'Ecoli Cells: {Ecoli.count} | ', end='')
        print(f'Structure Cells: {Structure.count} | ')
        print(f'Hunter Killer: {HunterKiller.count} | ', end='')
        print(f'Hunter Killer Kill Count: {HunterKiller.kill_count}')

    def tick(self):
        self.world_state.append(self.__repr__())
        self.counter += 1

        iteration_array = list(self.all_cells)

        for cell in iteration_array:
            if cell.lifespan <= 0:
                cell.reduce_count()
                self.available_positions.append((cell.x, cell.y))
                self.all_cells.remove(cell)
                continue
            else:
                cell.lifespan -= 1

            if cell.symbol == 'e':

                if self.counter % 3 == 0:
                    for replication_cell in replication_cells:
                        test_pos = (cell.x + replication_order[replication_cell][0],
                                    cell.y + replication_order[replication_cell][1])
                        if test_pos in self.available_positions:
                            self.add_to_world(Ecoli(position=test_pos))
                            break

                for i, j in product(range(-4, 5), range(-4, 5)):
                    if (i, j) == (0, 0):
                        continue
                    target_pos = (cell.x + i, cell.y + j)
                    if target_pos[0] >= self.SIZE or target_pos[1] >= self.SIZE or target_pos[0] < 0 or target_pos[
                        1] < 0:
                        continue
                    if self.world[target_pos] == 'x':
                        HunterKiller.kill_count += 1
                        self.available_positions.append((cell.x, cell.y))
                        cell.reduce_count()
                        self.all_cells.remove(cell)
                        break

            if cell.symbol == 'x':
                if self.counter > 10:
                    cell.symbol = 'x'

            if cell.symbol == 'S':
                continue

            new_pos = cell.intended_position()
            if new_pos in self.available_positions:
                self.available_positions.remove(new_pos)
                self.available_positions.append((cell.x, cell.y))
                cell.set_location(new_pos)

        self.update_world()

    def begin_simulation(self, max_iterations=100000, delay=0.01, movement=False):
        self.max_iterations = max_iterations
        while self._has_world_changed() and self.counter < self.max_iterations:
            self.print_header()
            print(self)
            print('\n')
            self.tick()
            sleep(delay)
            if not movement:
                break

    def simulate_n_steps(self, delay=0.1, iterations = 1):
        for _ in range(iterations):
            self.print_header()
            print(self)
            print('\n')
            self.tick()
            sleep(delay)


# ---------------------------------------------------------------------------
# Helper
# ---------------------------------------------------------------------------

def add_random_cells(petri_dish, cell_class, n):
    """
    Create n cells of cell_class at random free positions and add them.

    choice() is called fresh on every loop pass, after the previous
    add_to_world() removed its square, so two cells never land on the
    same spot.
    """
    for _ in range(n):
        position = choice(petri_dish.available_positions)
        petri_dish.add_to_world(cell_class(position=position))


# ---------------------------------------------------------------------------
# Activity 1
# ---------------------------------------------------------------------------

def activity1_task1():
    """Create a size-5 dish and run the simulation."""
    petri_dish = PetriDish(size=5)
    petri_dish.begin_simulation()
    return petri_dish


def activity1_task2():
    """Place four base Cells on the diagonal of a size-30 dish."""
    petri_dish = PetriDish(size=30)
    for position in [(0, 0), (5, 5), (10, 10), (15, 15)]:
        petri_dish.add_to_world(Cell(position=position))
    petri_dish.begin_simulation()
    return petri_dish


def activity1_task3():
    """Place 10 base Cells at random free positions."""
    seed(SEED_NUMBER) #do not alter this
    petri_dish = PetriDish(size=30)
    add_random_cells(petri_dish, Cell, 10)
    petri_dish.begin_simulation()
    return petri_dish


# ---------------------------------------------------------------------------
# Activity 2
# ---------------------------------------------------------------------------

def activity2_task1():
    seed(1) #do not alter this
    petri_dish = PetriDish(size=30)
    add_random_cells(petri_dish, Generic, 10)
    petri_dish.begin_simulation()
    return petri_dish


def activity2_task2():
    seed(2) #do not alter this
    petri_dish = PetriDish(size=30)
    add_random_cells(petri_dish, Ecoli, 10)
    petri_dish.begin_simulation()
    return petri_dish


def activity2_task3():
    seed(3) #do not alter this
    petri_dish = PetriDish(size=30)
    add_random_cells(petri_dish, Structure, 10)
    petri_dish.begin_simulation()
    return petri_dish


def activity2_task4():
    seed(4) #do not alter this
    petri_dish = PetriDish(size=30)
    add_random_cells(petri_dish, HunterKiller, 10)
    petri_dish.begin_simulation()
    return petri_dish


def activity2_task5():
    """10 of each type, created strictly in the listed order."""
    seed(SEED_NUMBER) #do not alter this
    petri_dish = PetriDish(size=30)
    for cell_class in [Cell, Generic, Ecoli, Structure, HunterKiller]:
        add_random_cells(petri_dish, cell_class, 10)
    petri_dish.begin_simulation()
    return petri_dish


# ---------------------------------------------------------------------------
# Activity 3
# ---------------------------------------------------------------------------

def activity3_task1():
    """Expected: 60 10 20 0 30"""
    seed(SEED_NUMBER) #do not alter this
    petri_dish = PetriDish(size=30)
    add_random_cells(petri_dish, Generic, 10)
    add_random_cells(petri_dish, Ecoli, 20)
    add_random_cells(petri_dish, HunterKiller, 30)

    print(Cell.count, Generic.count, Ecoli.count, Structure.count, HunterKiller.count)
    return Cell.count, Generic.count, Ecoli.count, Structure.count, HunterKiller.count


def activity3_task2a():
    activity3_task1()
    activity3_task1()

    return Cell.count, Generic.count, Ecoli.count, Structure.count, HunterKiller.count


def activity3_task2b():
    activity3_task1()
    reset_all_cell_counts()
    activity3_task1()

    return Cell.count, Generic.count, Ecoli.count, Structure.count, HunterKiller.count


def activity3_task3():
    """Expected: 50 5 15 0 30"""
    seed(SEED_NUMBER) #do not alter this
    petri_dish = PetriDish(size=30)
    add_random_cells(petri_dish, Generic, 10)
    add_random_cells(petri_dish, Ecoli, 20)
    add_random_cells(petri_dish, HunterKiller, 30)

    for _ in range(5):
        Generic.reduce_count()
    for _ in range(5):
        Ecoli.reduce_count()

    print(Cell.count, Generic.count, Ecoli.count, Structure.count, HunterKiller.count)
    return Cell.count, Generic.count, Ecoli.count, Structure.count, HunterKiller.count


def activity3_task4():
    """Step one tick, then show each cell's remaining lifespan."""
    seed(SEED_NUMBER) #do not alter this
    petri_dish = PetriDish(size=30)
    add_random_cells(petri_dish, Generic, 10)
    add_random_cells(petri_dish, Ecoli, 20)
    add_random_cells(petri_dish, HunterKiller, 30)
    petri_dish.simulate_n_steps()

    print([i.lifespan for i in petri_dish.all_cells])
    return petri_dish


def activity3_task5():
    """Full simulation with movement enabled."""
    seed(SEED_NUMBER)  # do not alter this
    reset_all_cell_counts() # do not alter this
    petri_dish = PetriDish(size=30)
    add_random_cells(petri_dish, Generic, 25)
    add_random_cells(petri_dish, Ecoli, 75)
    add_random_cells(petri_dish, HunterKiller, 13)
    add_random_cells(petri_dish, Structure, 100)
    petri_dish.begin_simulation(movement=True)

    return petri_dish


# ---------------------------------------------------------------------------
# Activity 4 (Task 14)
# ---------------------------------------------------------------------------

def activity4_task1():
    """KnightVirus cells hopping around among the original population."""
    seed(SEED_NUMBER)
    reset_all_cell_counts()
    petri_dish = PetriDish(size=30)
    add_random_cells(petri_dish, Generic, 25)
    add_random_cells(petri_dish, Ecoli, 75)
    add_random_cells(petri_dish, HunterKiller, 13)
    add_random_cells(petri_dish, Structure, 100)
    add_random_cells(petri_dish, KnightVirus, 15)
    petri_dish.begin_simulation(movement=True)
    print(f'Viruses alive: {Virus.count} (knight: {KnightVirus.count})')
    return petri_dish


if __name__ == '__main__':

    # uncomment the relevant task as needed. Complete the tasks in order.


    # activity1_task1()
    # activity1_task2()
    # activity1_task3()
    #
    # activity2_task1()
    # activity2_task2()
    # activity2_task3()
    # activity2_task4()
    # activity2_task5()
    #
    # activity3_task1()
    # activity3_task2a()
    # activity3_task2b()
    # activity3_task3()
    # activity3_task4()
    # activity3_task5()
    #
    # activity4_task1()
    pass