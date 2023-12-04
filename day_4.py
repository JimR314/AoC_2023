import AoC_Lib

def part_one(lines):
    total_points = 0
    for line in lines:
        # Splitting the line at the colon and using the second part
        _, card_data = line.split(": ")
        winning_numbers, my_numbers = card_data.split(" | ")
        winning_numbers = set(map(int, winning_numbers.split()))
        my_numbers = list(map(int, my_numbers.split()))

        matches = sum(num in winning_numbers for num in my_numbers)
        if matches > 0:
            points = 2 ** (matches - 1)  # 1 point for the first, double for each additional
            total_points += points

    return total_points

# Rest of the code remains the same


def part_two(lines):
    original_cards = parse_cards(lines)
    card_instances = [1] * len(original_cards)  # Start with 1 instance of each card

    # Process each card, including copies
    for i, card in enumerate(original_cards):
        matches = sum(num in card['winning_numbers'] for num in card['my_numbers'])
        for j in range(1, matches + 1):
            if i + j < len(original_cards):
                card_instances[i + j] += card_instances[i]

    return sum(card_instances)

def parse_cards(lines):
    cards = []
    for line in lines:
        _, card_data = line.split(": ")
        winning_numbers, my_numbers = card_data.split(" | ")
        winning_numbers = set(map(int, winning_numbers.split()))
        my_numbers = list(map(int, my_numbers.split()))
        cards.append({'winning_numbers': winning_numbers, 'my_numbers': my_numbers})
    return cards

def main():
    lines = AoC_Lib.parse_input(4)
    print(part_one(lines))
    print(part_two(lines))

if __name__ == '__main__':
    main()