import AoC_Lib

def parse_mappings(lines):
    mappings = []
    for line in lines:
        if line and not line.endswith(':'):
            parts = list(map(int, line.split()))
            mappings.append(parts)
    return mappings

def apply_mapping(number, mappings):
    for dest_start, src_start, length in mappings:
        if src_start <= number < src_start + length:
            return dest_start + (number - src_start)
    return number

def part_one(lines):
    sections = [[]]
    for line in lines:
        if line.endswith(':'):
            sections.append([])
        else:
            sections[-1].append(line)

    seeds = list(map(int, sections[0][0].split(': ')[1].split()))
    
    final_locations = []
    for seed in seeds:
        current_number = seed
        for section in sections[1:]:
            mappings = parse_mappings(section)
            current_number = apply_mapping(current_number, mappings)
        final_locations.append(current_number)

    return min(final_locations)

def parse_seed_ranges(line):
    parts = list(map(int, line.split(': ')[1].split()))
    ranges = [(parts[i], parts[i + 1]) for i in range(0, len(parts), 2)]
    return ranges

def split_ranges(ranges, mapping):
    new_ranges = []
    for start, length in ranges:
        end = start + length
        range_processed = False

        for dest_start, src_start, src_length in mapping:
            src_end = src_start + src_length

            if start < src_end and end > src_start:
                range_processed = True

                if start < src_start:
                    new_ranges.append((start, src_start - start))

                overlap_start = max(start, src_start)
                overlap_end = min(end, src_end)
                new_start = dest_start + (overlap_start - src_start)
                new_ranges.append((new_start, overlap_end - overlap_start))
                start = overlap_end

        if not range_processed or start < end:
            new_ranges.append((start, end - start))

    return new_ranges

def part_two(lines):
    sections = [[]]
    for line in lines:
        if line.endswith(':'):
            sections.append([])
        else:
            sections[-1].append(line)

    seed_ranges = parse_seed_ranges(sections[0][0])

    for section in sections[1:]:
        mappings = parse_mappings(section)
        seed_ranges = split_ranges(seed_ranges, mappings)

    final_locations = [(start, length) for start, length in seed_ranges]

    return min(final_locations, key=lambda x: x[0])[0]

def main():
    sample_input = AoC_Lib.parse_input(5, False)
    my_input = AoC_Lib.parse_input(5, True)
    print(f"Sample input, part one: {part_one(sample_input)}")
    print(f"Sample input, part two: {part_two(sample_input)}")
    print(f"My input, part one: {part_one(my_input)}")
    print(f"My input, part one: {part_two(my_input)}")

if __name__ == '__main__':
    main()