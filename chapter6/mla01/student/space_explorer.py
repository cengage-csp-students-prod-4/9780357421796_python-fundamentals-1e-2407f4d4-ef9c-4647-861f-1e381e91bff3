from random import seed, sample, choice
from os import linesep
from string import punctuation
from math import sqrt
from itertools import product

SEED_NUMBER = 1024
seed(SEED_NUMBER)
MAP_SIZE = 100
all_possible_symbols = frozenset(punctuation+'GSFT ')

# Extension (Task 13) constants
STARTING_FUEL = 50
FUEL_PER_PICKUP = 15


def define_possible_objects(choices=punctuation):
    chars = choices
    chars += 'G'
    chars += 'T'*3
    chars += 'F'*3
    return chars


def generate_object(itera, available_coordinates, occupied_coordinates):
    symbol = sample(itera, 1)
    coordinates = choice(available_coordinates)
    available_coordinates.remove(coordinates)
    occupied_coordinates.append(coordinates)
    return symbol, coordinates


def set_up():
    symbols1 = define_possible_objects(punctuation)
    symbols2 = define_possible_objects('^&*'*5)
    return symbols1, symbols2


def clean_symbol(symbol):
    # sample() returns a list like ['F']; normalize to a plain string so
    # comparisons work whether a symbol arrives as 'F' or ['F'].
    return ''.join(symbol) if isinstance(symbol, list) else symbol


# ---------------------------------------------------------------------------
# Task 1: build every (x, y) coordinate on a map_size x map_size grid
# ---------------------------------------------------------------------------
def generate_available_coordinates(map_size):
    # product(range(n), range(n)) yields (0,0), (0,1), ... (n-1, n-1).
    # x is the outer loop, so the order is deterministic. This matters because
    # the seeded random.choice() picks by index. Must be a list (not a set)
    # because generate_object() calls choice() and .remove() on it.
    return list(product(range(map_size), range(map_size)))


# ---------------------------------------------------------------------------
# Task 2: map every coordinate to a blank space, with the ship 'S' at (0, 0)
# ---------------------------------------------------------------------------
def generate_empty_map(available_coordinates):
    # dict.fromkeys gives every key the same starting value: a single space.
    # Tuples work as dict keys because they are immutable and hashable.
    galaxy_map = dict.fromkeys(available_coordinates, ' ')
    galaxy_map[(0, 0)] = 'S'  # starting position of the spacecraft
    return galaxy_map


# ---------------------------------------------------------------------------
# Task 3: unique symbols on the map (including 'S' and ' ')
# ---------------------------------------------------------------------------
def get_unique_objects(galaxy_map):
    # A set drops duplicates automatically; frozenset makes it immutable.
    return frozenset(galaxy_map.values())


# ---------------------------------------------------------------------------
# Task 8: symbols from the full symbol pool that never appeared in the galaxy
# ---------------------------------------------------------------------------
def symbols_not_used_in_galaxy(symbols_in_galaxy):
    # .difference() accepts ANY iterable (list, set, string, frozenset).
    # The '-' operator requires both sides to be sets and raises TypeError
    # otherwise.
    return frozenset(all_possible_symbols.difference(symbols_in_galaxy))


# ---------------------------------------------------------------------------
# Task 11 (common_objects_encountered): symbols found in BOTH galaxies
# ---------------------------------------------------------------------------
def common_objects_encountered(galaxy_1_objects, galaxy_2_objects):
    # Intersection: only elements present in both sets.
    return galaxy_1_objects & galaxy_2_objects


# ---------------------------------------------------------------------------
# Task 9: symbols in galaxy 1 but not in galaxy 2
# ---------------------------------------------------------------------------
def objects_encountered_in_galaxy1_not_galaxy2(galaxy_1_objects, galaxy_2_objects):
    return galaxy_1_objects - galaxy_2_objects


# ---------------------------------------------------------------------------
# Task 10: symbols in galaxy 2 but not in galaxy 1
# ---------------------------------------------------------------------------
def objects_encountered_in_galaxy2_not_galaxy1(galaxy_1_objects, galaxy_2_objects):
    return galaxy_2_objects - galaxy_1_objects


# ---------------------------------------------------------------------------
# Task 12: every symbol seen in EITHER galaxy
# ---------------------------------------------------------------------------
def objects_encountered_in_both_galaxys(galaxy1_objects, galaxy2_objects):
    # Union: all elements from both sets, no duplicates.
    return galaxy1_objects | galaxy2_objects


# ---------------------------------------------------------------------------
# Task 7: fuel ('F') and treasure ('T') strictly closer than the goal ('G')
# ---------------------------------------------------------------------------
def calculate_path_to_goal(sorted_object_list):
    # Distance to the goal. If there is no 'G', treat the goal as infinitely
    # far away, so every F/T counts as closer.
    goal_distance = float('inf')
    for distance, coordinates, symbol in sorted_object_list:
        if clean_symbol(symbol) == 'G':
            goal_distance = distance
            break

    path_list = list()
    for obj in sorted_object_list:
        distance, coordinates, symbol = obj
        if clean_symbol(symbol) in ('F', 'T') and distance < goal_distance:
            path_list.append(obj)   # keep the original tuple unchanged

    return sorted(path_list, key=lambda item: item[0])  # sort by distance only


# ---------------------------------------------------------------------------
# Task 4: flatten the map into one string, in coordinate order
# ---------------------------------------------------------------------------
def display_galaxy(galaxy_map):
    # Dicts preserve insertion order (Python 3.7+), so this follows the
    # order from generate_available_coordinates. ''.join is faster than
    # repeated += because strings are immutable (each += builds a new string).
    return ''.join(galaxy_map[coordinates] for coordinates in galaxy_map)


# ---------------------------------------------------------------------------
# Task 5: straight-line distance from (0, 0), truncated to an int
# ---------------------------------------------------------------------------
def calculate_euclidean_distance(coordinates):
    # Index instead of unpacking, so this still works if the grader passes
    # a list [x, y] or a longer sequence instead of an (x, y) tuple.
    x = coordinates[0]
    y = coordinates[1]
    distance = sqrt((x ** 2) + (y ** 2))
    return int(distance)


# ---------------------------------------------------------------------------
# Task 6: keep receiving objects until the goal 'G' shows up
# ---------------------------------------------------------------------------
def populate_galaxy_map(available_symbols, available_coordinates, occupied_coordinates, galaxy_map):
    objects_encountered_list = list()
    while True:
        symbol, coordinates = generate_object(available_symbols, available_coordinates, occupied_coordinates)
        distance = calculate_euclidean_distance(coordinates)

        # sample() returns a LIST like ['G'], so pull out the string itself.
        symbol = symbol[0]

        # Record the object and place it on the map.
        objects_encountered_list.append((distance, coordinates, symbol))
        galaxy_map[coordinates] = symbol

        # The goal is recorded before breaking, because
        # calculate_path_to_goal needs it to know the cutoff distance.
        if symbol == 'G':
            break

    # Tuples sort by their first element (distance) first; ties fall back to
    # coordinates, which keeps the order deterministic.
    return sorted(objects_encountered_list)


# ---------------------------------------------------------------------------
# Task 13 (extension): is there enough fuel to reach the goal?
# Simplified model: the ship flies straight from (0, 0) to the goal, and
# collects every 'F' that is closer than the goal along the way.
# ---------------------------------------------------------------------------
def has_enough_fuel(sorted_object_list, path_list):
    goal_distance = next((d for d, _, s in sorted_object_list if clean_symbol(s) == 'G'), None)
    if goal_distance is None:
        return False, STARTING_FUEL

    fuel_pickups = sum(1 for _, _, s in path_list if clean_symbol(s) == 'F')
    total_fuel = STARTING_FUEL + fuel_pickups * FUEL_PER_PICKUP
    return total_fuel >= goal_distance, total_fuel


def run_exploration():
    available_symbols1, available_symbols2 = set_up()

    available_coordinates1 = generate_available_coordinates(MAP_SIZE)
    available_coordinates2 = generate_available_coordinates(MAP_SIZE)
    occupied_coordinates1 = list()
    occupied_coordinates2 = list()

    galaxy_map_1 = generate_empty_map(available_coordinates1)
    galaxy_map_2 = generate_empty_map(available_coordinates2)

    explorer1_list = populate_galaxy_map(available_symbols1, available_coordinates1, occupied_coordinates1, galaxy_map_1)
    explorer2_list = populate_galaxy_map(available_symbols2, available_coordinates2, occupied_coordinates2, galaxy_map_2)

    print(explorer1_list)
    print(explorer2_list)

    path_list1 = calculate_path_to_goal(explorer1_list)
    print(path_list1)

    path_list2 = calculate_path_to_goal(explorer2_list)
    print(path_list2)

    display_galaxy(galaxy_map_1)
    display_galaxy(galaxy_map_2)
    galaxy2_symbols = get_unique_objects(galaxy_map_2)
    galaxy1_symbols = get_unique_objects(galaxy_map_1)
    print(galaxy1_symbols)
    print(galaxy2_symbols)

    # --- Mission analysis ---
    print('Unused in galaxy 1:', symbols_not_used_in_galaxy(galaxy1_symbols))
    print('Unused in galaxy 2:', symbols_not_used_in_galaxy(galaxy2_symbols))
    print('Only in galaxy 1:', objects_encountered_in_galaxy1_not_galaxy2(galaxy1_symbols, galaxy2_symbols))
    print('Only in galaxy 2:', objects_encountered_in_galaxy2_not_galaxy1(galaxy1_symbols, galaxy2_symbols))
    print('Common to both:', common_objects_encountered(galaxy1_symbols, galaxy2_symbols))
    print('In either galaxy:', objects_encountered_in_both_galaxys(galaxy1_symbols, galaxy2_symbols))

    # --- Extension: fuel check ---
    for name, objects, path in (('Mission 1', explorer1_list, path_list1),
                                ('Mission 2', explorer2_list, path_list2)):
        ok, fuel = has_enough_fuel(objects, path)
        print(f'{name}: fuel available {fuel} -> {"reaches goal" if ok else "runs out"}')


# ---------------------------------------------------------------------------
# Quick self-tests (call run_tests() manually; not run by the grader)
# ---------------------------------------------------------------------------
def run_tests():
    coords = generate_available_coordinates(3)
    assert len(coords) == 9 and coords[0] == (0, 0) and coords[-1] == (2, 2)
    assert len(generate_available_coordinates(100)) == 10000

    m = generate_empty_map(coords)
    assert m[(0, 0)] == 'S' and m[(2, 2)] == ' ' and len(m) == 9

    m[(1, 1)] = '^'
    assert get_unique_objects(m) == frozenset({'S', ' ', '^'})
    assert display_galaxy(m) == 'S   ^    '

    assert calculate_euclidean_distance((1, 2)) == 2
    assert calculate_euclidean_distance((3, 4)) == 5
    assert isinstance(calculate_euclidean_distance((1, 1)), int)

    sample_list = [(1, (1, 0), 'F'), (2, (2, 0), '^'), (3, (3, 0), 'T'),
                   (4, (4, 0), 'G'), (5, (5, 0), 'F')]
    assert calculate_path_to_goal(sample_list) == [(1, (1, 0), 'F'), (3, (3, 0), 'T')]

    a, b = frozenset('SGx'), frozenset('SGy')
    assert objects_encountered_in_galaxy1_not_galaxy2(a, b) == {'x'}
    assert objects_encountered_in_galaxy2_not_galaxy1(a, b) == {'y'}
    assert common_objects_encountered(a, b) == {'S', 'G'}
    assert objects_encountered_in_both_galaxys(a, b) == {'S', 'G', 'x', 'y'}
    # Robustness checks for the shapes a grader might send
    assert calculate_euclidean_distance([1, 2]) == 2
    list_symbols = [(1, (1, 0), ['F']), (4, (4, 0), ['G']), (5, (5, 0), ['T'])]
    assert calculate_path_to_goal(list_symbols) == [(1, (1, 0), ['F'])]
    assert calculate_path_to_goal([(2, (2, 0), 'T'), (1, (1, 0), 'F')]) == [(1, (1, 0), 'F'), (2, (2, 0), 'T')]
    assert symbols_not_used_in_galaxy(list(all_possible_symbols)) == frozenset()
    assert 'G' in symbols_not_used_in_galaxy({'S', ' '})
    print('All tests passed.')


if __name__ == '__main__':
    run_exploration()