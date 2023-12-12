import AoC_Lib

def parse_input(input_data):
    galaxies = []
    empty_rows, empty_cols = set(range(len(input_data))), set(range(len(input_data[0])))
    
    for i, row in enumerate(input_data):
        for j, cell in enumerate(row):
            if cell == '#':
                galaxies.append((i, j))
                empty_rows.discard(i)
                empty_cols.discard(j)
    
    return galaxies, empty_rows, empty_cols

def expand_coordinates(galaxies, empty_rows, empty_cols):
    expanded_galaxies = []
    for x, y in galaxies:
        expanded_x = x + sum(1 for row in empty_rows if row < x)
        expanded_y = y + sum(1 for col in empty_cols if col < y)
        expanded_galaxies.append((expanded_x, expanded_y))
    return expanded_galaxies

def sum_shortest_paths(galaxies):
    total_length = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            x1, y1 = galaxies[i]
            x2, y2 = galaxies[j]
            total_length += abs(x1 - x2) + abs(y1 - y2)
    return total_length

def part_one(input_data):
    galaxies, empty_rows, empty_cols = parse_input(input_data)
    expanded_galaxies = expand_coordinates(galaxies, empty_rows, empty_cols)
    return sum_shortest_paths(expanded_galaxies)

def calculate_initial_distances(galaxies):
    distances = {}
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            x1, y1 = galaxies[i]
            x2, y2 = galaxies[j]
            distances[(i, j)] = (abs(x1 - x2), abs(y1 - y2))
    return distances

def count_expansions(galaxies, distances, empty_rows, empty_cols):
    total_length = 0
    expansion_factor = 1000000 - 1
    for (i, j), (dx, dy) in distances.items():
        x_expansions = sum(1 for row in empty_rows if galaxies[i][0] < row < galaxies[j][0] or galaxies[j][0] < row < galaxies[i][0])
        y_expansions = sum(1 for col in empty_cols if galaxies[i][1] < col < galaxies[j][1] or galaxies[j][1] < col < galaxies[i][1])
        total_length += (dx + x_expansions * expansion_factor) + (dy + y_expansions * expansion_factor)
    return total_length

def part_two(input_data):
    galaxies, empty_rows, empty_cols = parse_input(input_data)
    distances = calculate_initial_distances(galaxies)
    return count_expansions(galaxies, distances, empty_rows, empty_cols)

def main():
    sample_input = AoC_Lib.parse_input(11, False)
    my_input = AoC_Lib.parse_input(11, True)
    print(f"Sample input, part one: {part_one(sample_input)}")
    print(f"Sample input, part two: {part_two(sample_input)}")
    print(f"My input, part one: {part_one(my_input)}")
    print(f"My input, part two: {part_two(my_input)}")

if __name__ == '__main__':
    main()