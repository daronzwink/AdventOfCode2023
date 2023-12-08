#!/usr/bin/env python3

import argparse


def map_number(number, mapping):
    """
    Returns the mapped number for the given mapping.
    """
    for line in mapping:
        dest_start, src_start, length = map(int, line.split())
        if src_start <= number < src_start + length:
            return dest_start + (number - src_start)
    return number

def main():
    """
    Main function
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--example', action='store_true')
    args = parser.parse_args()

    data_file = 'day05_example.dat' if args.example else 'day05.dat'

    part1_answer = 0
    part2_answer = 0
    with open(data_file, 'r', encoding='utf-8') as file:

        # Read in the data
        data = file.read().splitlines()
        data = '\n'.join(data)
        sections = data.split('\n\n')
        seeds = list(map(int, sections[0].split(': ')[1].split()))
        mappings = [section.split('\n')[1:] for section in sections[1:]]

        # Process Part 1
        for seed in seeds:
            location = seed
            for mapping in mappings:
                location = map_number(location, mapping)
            if part1_answer == 0 or location < part1_answer:
                part1_answer = location

        # Process Part 2
        seed_ranges = list(map(int, sections[0].split(': ')[1].split()))
        seeds = [i for start, length in zip(seed_ranges[::2], seed_ranges[1::2]) for i in range(start, start + length)]
        for seed in seeds:
            location = seed
            for mapping in mappings:
                location = map_number(location, mapping)
            if part2_answer == 0 or location < part2_answer:
                part2_answer = location

    print(f"Answer (Part 1): {part1_answer}")
    print(f"Answer (Part 2): {part2_answer}")

if __name__ == "__main__":
    main()
