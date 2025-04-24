import sys
import re
from collections import defaultdict


def parse_design(line):
    """
    Parse a single bouquet design line into its components.
    Returns a dictionary with:
        name: Design name (A-Z)
        size: Flower size ('L' or 'S')
        species_max: Dict of species -> max quantity allowed
        total: Total flowers in bouquet
        species_order: List of species in order
    """
    if len(line) < 2:
        raise ValueError("Invalid design line: too short")
    design_name = line[0]
    size = line[1]
    remaining = line[2:]

    # Extract the total quantity (digits at the end)
    total_str = ''
    i = len(remaining) - 1
    while i >= 0 and remaining[i].isdigit():
        total_str = remaining[i] + total_str
        i -= 1
    if not total_str:
        raise ValueError(f"Invalid design line '{line}': no total found")
    total = int(total_str)
    pairs_part = remaining[:i+1]

    # Extract pairs of <max_qty><species>
    pairs = re.findall(r'(\d+)([a-z])', pairs_part)
    if not pairs:
        raise ValueError(f"Invalid design line '{line}': no species found")
    species_max = {}
    for qty_str, species in pairs:
        qty = int(qty_str)
        species_max[species] = qty

    return {
        'name': design_name,
        'size': size,
        'species_max': species_max,
        'total': total,
        'species_order': sorted(species_max.keys()),  # Always in alpha order
    }


def find_valid_combination(available_counts, max_counts, total, species_order):
    """
    Try to find a valid combination of flowers for a bouquet design.
    available_counts: dict of species -> available count
    max_counts: dict of species -> max allowed by design
    total: total flowers required
    species_order: list of species (to keep output order consistent)
    Returns a dict of species -> count to use, or None if impossible.
    """
    combination = {}
    remaining = total
    num_species = len(species_order)

    # assign as many as possible to each species, in order,
    for i, s in enumerate(species_order):
        max_possible = min(available_counts.get(s, 0), max_counts[s])
        if max_possible < 1:
            return None  # Not enough of this species
        minimal_remaining = (num_species - i - 1)
        max_assignable = min(max_possible, remaining - minimal_remaining)
        if max_assignable < 1:
            return None  # Can't assign at least one
        assigned = max_assignable
        combination[s] = assigned
        remaining -= assigned

    if remaining != 0:
        return None  # Did not reach required total

    # Final check: all counts within available and max
    for s in species_order:
        if combination[s] > available_counts.get(s, 0) or combination[s] > max_counts[s]:
            return None

    return combination


def main():
    """
    main function which calls all other functions and steps
    """
    # read bouquet designs from stdin until empty line
    designs = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            break
        designs.append(parse_design(line))

    # available flower storage[size][species] = count
    storage = defaultdict(lambda: defaultdict(int))

    # process incoming flowers, one per line
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        if len(line) < 2:
            continue
        species = line[0]
        size = line[1]
        storage[size][species] += 1

        # for each design, check if a bouquet can be made
        for design in designs:
            if design['size'] != size:
                continue  # Only use flowers of matching size

            required_species = design['species_max'].keys()
            available_in_size = storage[size]
            # Check if at least one of each required species is available
            all_present = all(available_in_size.get(s, 0) >= 1 for s in required_species)
            if not all_present:
                continue

            available_counts = {s: available_in_size.get(s, 0) for s in required_species}
            combination = find_valid_combination(
                available_counts,
                design['species_max'],
                design['total'],
                design['species_order']
            )

            if combination is not None:
                # remove used flowers from storage
                for s, qty in combination.items():
                    storage[size][s] -= qty
                    if storage[size][s] == 0:
                        del storage[size][s]

                # format bouquet output: <design name><size><qty1><species1>...
                bouquet = design['name'] + design['size']
                for s in design['species_order']:
                    bouquet += str(combination[s]) + s
                print(bouquet)
                break  # only one bouquet per flower arrival


if __name__ == "__main__":
    main()
