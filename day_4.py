import AoC_Lib

def part_one(lines):
    total_points = 0
    for line in lines:
        _, card_data = line.split(": ")
        winning_numbers, my_numbers = card_data.split(" | ")
        winning_numbers = set(map(int, winning_numbers.split()))
        my_numbers = list(map(int, my_numbers.split()))

        matches = sum(num in winning_numbers for num in my_numbers)
        if matches > 0:
            points = 2 ** (matches - 1)
            total_points += points

    return total_points


def part_two(lines):
    original_cards = parse_cards(lines)
    card_instances = [1] * len(original_cards)
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