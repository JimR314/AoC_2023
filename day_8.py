import AoC_Lib
import math
from functools import reduce
from collections import defaultdict 

def part_one(lines):
    instructions = lines[0]
    node_map = {}
    for line in lines[2:]:
        node, connections = line.split(' = ')
        left, right = connections.strip('()').split(', ')
        node_map[node] = (left, right)

    current_node = 'AAA'
    step_count = 0
    instruction_index = 0

    while current_node != 'ZZZ':
        if instructions[instruction_index] == 'L':
            current_node = node_map[current_node][0]
        else:
            current_node = node_map[current_node][1]

        instruction_index = (instruction_index + 1) % len(instructions)

        step_count += 1

    return step_count

def lcm(a, b):
    """Calculate the least common multiple of two numbers."""
    return abs(a*b) // math.gcd(a, b)

def calculate_min_step_count(cycle_info, z_positions):
    max_step_count = 0
    for node, (offset, cycle_length) in cycle_info.items():
        earliest_z_step = None
        for z_pos in z_positions[node]:
            step_count = offset + z_pos
            while step_count < offset:
                step_count += cycle_length
            if earliest_z_step is None or step_count < earliest_z_step:
                earliest_z_step = step_count

        max_step_count = max(max_step_count, earliest_z_step)

    return max_step_count


def part_two(lines):
    instructions = lines[0]
    node_map = {}
    for line in lines[2:]:
        node, connections = line.split(' = ')
        left, right = connections.strip('()').split(', ')
        node_map[node] = (left, right)

    starting_nodes = [node for node in node_map if node.endswith('A')]
    cycle_info = {} 
    z_positions = {node: set() for node in starting_nodes}  
    all_seen_states = {}  

    for start_node in starting_nodes:
        current_node = start_node
        instruction_index = 0
        seen_states = {}
        step_count = 0

        while True:
            if instructions[instruction_index] == 'L':
                next_node = node_map[current_node][0]
            else:
                next_node = node_map[current_node][1]
            next_instruction_index = (instruction_index + 1) % len(instructions)

            state = (next_node, next_instruction_index)
            if state in seen_states:
                cycle_start_step = seen_states[state]
                cycle_length = step_count - cycle_start_step
                cycle_info[start_node] = (cycle_start_step+1, cycle_length)
                all_seen_states[start_node] = seen_states

                for state, st_count in seen_states.items():
                    node, _ = state
                    if st_count >= cycle_start_step and node.endswith('Z'):
                        z_positions[start_node].add(st_count - cycle_start_step)
                break
            else:
                seen_states[state] = step_count
                current_node = next_node
                instruction_index = next_instruction_index
                step_count += 1

    print(cycle_info)
    print(z_positions)

    return calculate_min_step_count(cycle_info, z_positions)






def main():
    sample_input = AoC_Lib.parse_input(8, False)
    my_input = AoC_Lib.parse_input(8, True)
    print(f"Sample input, part one: {part_one(sample_input)}")
    print(f"Sample input, part two: {part_two(sample_input)}")
    print(f"My input, part one: {part_one(my_input)}")
    print(f"My input, part two: {part_two(my_input)}")

if __name__ == '__main__':
    main()