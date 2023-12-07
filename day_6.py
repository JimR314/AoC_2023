import AoC_Lib
import math

def part_one(lines):
    total_ways = 1
    times, distances = lines
    times = list(map(int, times.split()[1:]))  # Skip the first word 'Time:'
    distances = list(map(int, distances.split()[1:]))  # Skip the first word 'Distance:'

    for total_time, record_distance in zip(times, distances):
        # Solve the quadratic equation: t^2 - total_time*t + record_distance = 0
        a, b, c = 1, -total_time, record_distance

        # Calculate the discriminant
        discriminant = b**2 - 4*a*c

        # Find the two roots
        t1 = (-b - math.sqrt(discriminant)) / (2*a)
        t2 = (-b + math.sqrt(discriminant)) / (2*a)

        # Adjust start and end points
        start = math.ceil(min(t1, t2))
        end = math.floor(max(t1, t2))

        # Exclude the exact integer solutions that result in a draw
        if start == min(t1, t2):
            start += 1
        if end == max(t1, t2):
            end -= 1

        ways = max(0, end - start + 1)
        print(total_time, record_distance, ways)
        print(start, end)
        total_ways *= ways

    return total_ways

def part_two(lines):
    times, distances = lines
    total_time = int(times.replace("Time: ", "").replace(" ", ""))
    record_distance = int(distances.replace("Distance: ", "").replace(" ", ""))

    # Solve the quadratic equation: t^2 - total_time*t + record_distance = 0
    a, b, c = 1, -total_time, record_distance

    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Find the two roots
    t1 = (-b - math.sqrt(discriminant)) / (2*a)
    t2 = (-b + math.sqrt(discriminant)) / (2*a)

    # Adjust start and end points
    start = math.ceil(min(t1, t2))
    end = math.floor(max(t1, t2))

    # Exclude the exact integer solutions that result in a draw
    if start == min(t1, t2):
        start += 1
    if end == max(t1, t2):
        end -= 1

    ways = max(0, end - start + 1)

    return ways    

def main():
    sample_input = AoC_Lib.parse_input(6, False)
    my_input = AoC_Lib.parse_input(6, True)
    print(f"Sample input, part one: {part_one(sample_input)}")
    print(f"Sample input, part two: {part_two(sample_input)}")
    print(f"My input, part one: {part_one(my_input)}")
    print(f"My input, part one: {part_two(my_input)}")

if __name__ == '__main__':
    main()