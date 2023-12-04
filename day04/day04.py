#!/usr/bin/env python3

import argparse
from collections import deque


def calculate_points(cards):
    """
    Calculates the total number of points for all cards
    """
    total_points = 0
    for card in cards:
        _, numbers = card.split(':')
        winning_numbers, card_numbers = numbers.split('|')
        winning_numbers = set(map(int, winning_numbers.split()))
        card_numbers = list(map(int, card_numbers.split()))

        points = 0
        for number in card_numbers:
            if number in winning_numbers:
                points = points * 2 if points else 1
        total_points += points
    return total_points


def calculate_total_cards(cards):
    """
    Calculates the total number of cards that need to be printed
    """
    card_queue = deque([(i, card) for i, card in enumerate(cards)])
    total_cards = 0

    while card_queue:
        index, card = card_queue.popleft()
        _, numbers = card.split(':')
        winning_numbers, card_numbers = numbers.split('|')
        winning_numbers = set(map(int, winning_numbers.split()))
        card_numbers = list(map(int, card_numbers.split()))

        matches = sum(number in winning_numbers for number in card_numbers)
        total_cards += 1

        # Add copies of the next unique cards to the queue
        for i in range(1, matches + 1):
            try:
                card_queue.append((index + i, cards[index + i]))
            except IndexError:
                # No more cards to copy
                break

    return total_cards


def main():
    """
    Main function
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--example', action='store_true')
    args = parser.parse_args()

    data_file = 'day04_example.dat' if args.example else 'day04.dat'

    part1_total = 0
    part2_total = 0
    with open(data_file, 'r', encoding='utf-8') as file:

        # Read in the data
        cards = file.readlines()

        # Get answer for part 1
        part1_total = calculate_points(cards)

        # Get answer for part 2
        part2_total = calculate_total_cards(cards)

    print(f"Answer (Part 1): {part1_total}")
    print(f"Answer (Part 2): {part2_total}")


if __name__ == "__main__":
    main()
