import AoC_Lib
import itertools
from functools import cmp_to_key

def card_value(card):
    """ Returns the numerical value of a card. """
    values = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 10, 
              '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
    return values[card]

def hand_type(hand):
    """ Determine the type of the hand. """
    card_count = {card: hand.count(card) for card in hand}
    frequency_pattern = sorted(card_count.values(), reverse=True)
    hand_types = {(5,): 1, (4, 1): 2, (3, 2): 3, (3, 1, 1): 4, (2, 2, 1): 5, (2, 1, 1, 1): 6, (1, 1, 1, 1, 1): 7}
    return hand_types.get(tuple(frequency_pattern), 7)  # Default to High Card if not found

def compare_hands(hand1, hand2):
    type1 = hand_type(hand1)
    type2 = hand_type(hand2)

    if type1 < type2:
        return -1
    elif type1 > type2:
        return 1
    for card1, card2 in zip(hand1, hand2):
        value1, value2 = card_value(card1), card_value(card2)
        if value1 > value2:
            return -1
        elif value1 < value2:
            return 1

    return 0  # If completely equal

def bubble_sort_hands(hands):
    n = len(hands)
    print(n)
    for i in range(n):
        print(i)
        for j in range(0, n-i-1):
            if compare_hands_2(hands[j][0], hands[j+1][0]) > 0:
                hands[j], hands[j+1] = hands[j+1], hands[j]
    return hands

def part_one(lines):
    hands = [(hand.split()[0], int(hand.split()[1])) for hand in lines]
    sorted_hands = bubble_sort_hands(hands)

    total_winnings = sum(bid * (len(lines) - rank + 1) for rank, (_, bid) in enumerate(sorted_hands, start=1))

    print("Hands from strongest to weakest with rank:")
    for rank, (hand, bid) in enumerate(sorted_hands, start=1):
        print(f"Rank {rank}: {hand}, bid: {bid}")

    return total_winnings

def optimize_hand(hand):
    """ Returns the best possible hand type considering J as a wildcard. """
    joker_count = hand.count('J')
    if joker_count == 0:
        return hand  # No optimization needed if no joker

    non_joker_hand = [card for card in hand if card != 'J']
    if not non_joker_hand:
        return 'A' * joker_count

    most_freq_card = max(set(non_joker_hand), key=non_joker_hand.count)
    potential_hand = hand.replace('J', most_freq_card)
    best_hand_type = hand_type(potential_hand)
    best_hand = potential_hand

    replacement_cards = 'AKQ98765432'
    for replacements in itertools.product(replacement_cards, repeat=joker_count):
        temp_hand = list(hand)
        replacement_index = 0

        for i, card in enumerate(temp_hand):
            if card == 'J':
                temp_hand[i] = replacements[replacement_index]
                replacement_index += 1

        temp_hand_str = ''.join(temp_hand)
        temp_hand_type = hand_type(temp_hand_str)

        if temp_hand_type < best_hand_type:
            best_hand = temp_hand_str
            best_hand_type = temp_hand_type

    return best_hand

def compare_hands_2(hand1, hand2):
    optimized_hand1 = optimize_hand(hand1)
    optimized_hand2 = optimize_hand(hand2)
    type1 = hand_type(optimized_hand1)
    type2 = hand_type(optimized_hand2)

    if type1 < type2:
        return -1
    elif type1 > type2:
        return 1

    for card1, card2 in zip(hand1, hand2):
        value1, value2 = card_value(card1), card_value(card2)
        if value1 > value2:
            return -1
        elif value1 < value2:
            return 1

    return 0


def part_two(lines):
    hands = [(hand.split()[0], int(hand.split()[1])) for hand in lines]
    print("here1")
    sorted_hands = bubble_sort_hands(hands)
    print("here2")
    total_winnings = sum(bid * (len(lines) - rank + 1) for rank, (_, bid) in enumerate(sorted_hands, start=1))
    print("here3")
    print("Hands from strongest to weakest with rank (Part Two):")
    for rank, (hand, bid) in enumerate(sorted_hands, start=1):
        print(f"Rank {rank}: {hand}, bid: {bid}")

    return total_winnings

# TOO LOW 251156055
# TOO LOW 251481660

def main():
    sample_input = AoC_Lib.parse_input(7, False)
    my_input = AoC_Lib.parse_input(7, True)
    # print(f"Sample input, part one: {part_one(sample_input)}")
    print(f"Sample input, part two: {part_two(sample_input)}")
    # print(f"My input, part one: {part_one(my_input)}")
    print(f"My input, part two: {part_two(my_input)}")
    print(compare_hands_2('KTJJT', 'T55J5'))

if __name__ == '__main__':
    main()