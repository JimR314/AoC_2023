def parse_input(day):
    lines = []
    with open(f"C://Users//Jim//Coding//AoC_2023//day_{day}.txt", "r") as f:
        l = f.readlines()
        for line in l:
            lines.append(line.strip())
        return lines

def part_one(lines):
    total = 0
    symbols = set()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != '.' and char.isdigit() == False:
                symbols.add((x, y))
    
    for y, line in enumerate(lines):
        in_num = False
        curr_num = ''
        valid_num = False
        for x, char in enumerate(line):
            if char.isdigit():
                curr_num += char
                if in_num == False:
                    in_num = True
                if x == len(line) - 1:
                    num_len = len(curr_num)
                    for i in range(num_len + 1):
                        for j in range(3):
                            if 0 <= x - i <= len(line) - 1 and 0 <= y + j - 1 <= len(lines) - 1:
                                if (x - i, y + j - 1) in symbols:
                                    valid_num = True
                                    break
                        if valid_num:
                            break
                    if valid_num:
                        total += int(curr_num)
                    
            elif in_num:
                in_num = False
                num_len = len(curr_num)
                for i in range(num_len + 2):
                    for j in range(3):
                        if 0 <= x - i <= len(line) - 1 and 0 <= y + j - 1 <= len(lines) - 1:
                            if (x - i, y + j - 1) in symbols:
                                valid_num = True
                                break
                    if valid_num:
                        break
                if valid_num:
                    total += int(curr_num)
                curr_num = ''
                valid_num = False
    return total
                       
import re            

def part_two(lines):
    def process_line(line):
        result = []
        start_index = 0
        for match in re.finditer(r'\d+|\D', line):
            segment = match.group()
            if segment != '.':
                start_index = match.start()
                result.append((segment, start_index))

        return result
    
    def process_input(lines):
        return [process_line(line) for line in lines]

    def find_gears(processed_lines):
        gears = {}
        for y, line in enumerate(processed_lines):
            for segment, x in line:
                if '*' in segment:
                    gears[(x + segment.index('*'), y)] = []

        return gears

    def get_adjacent_numbers(processed_lines, gears):
        for gx, gy in gears:
            adjacent_numbers = []
            checked_positions = set()
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = gx + dx, gy + dy
                    if 0 <= ny < len(processed_lines) and (nx, ny) not in checked_positions:
                        for segment, sx in processed_lines[ny]:
                            if sx <= nx < sx + len(segment) and segment.isdigit():
                                adjacent_numbers.append(int(segment))
                                # Mark all positions of this number as checked
                                for pos in range(sx, sx + len(segment)):
                                    checked_positions.add((pos, ny))
            if len(adjacent_numbers) == 2:
                gears[(gx, gy)] = adjacent_numbers
            else:
                gears[(gx, gy)] = []

    def calculate_gear_ratios(gears):
        return sum(a * b for numbers in gears.values() if len(numbers) == 2 for a, b in [numbers])

    processed_lines = process_input(lines)
    gears = find_gears(processed_lines)
    get_adjacent_numbers(processed_lines, gears)
    total_gear_ratios = calculate_gear_ratios(gears)
    return total_gear_ratios


def main():
    lines = parse_input(3)
    print(part_one(lines))
    print(part_two(lines))

if __name__ == "__main__":
    main()