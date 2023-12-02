#!/usr/bin/env python3

import argparse

def parse_game_data(line):
    """
    Parses the game data from the given line
    """
    game_id, rounds = line.split(': ')
    game_id = int(game_id.split(' ')[1])
    rounds = rounds.split('; ')
    round_data = []
    for round in rounds:
        cubes = round.split(', ')
        red = sum(int(c.split(' ')[0]) for c in cubes if 'red' in c)
        green = sum(int(c.split(' ')[0]) for c in cubes if 'green' in c)
        blue = sum(int(c.split(' ')[0]) for c in cubes if 'blue' in c)
        round_data.append((red, green, blue))
    return game_id, round_data

def is_game_possible(game, red_cubes, green_cubes, blue_cubes):
    """
    Returns True if the game is possible with the given number of cubes
    """
    for round in game[1]:
        if round[0] > red_cubes or round[1] > green_cubes or round[2] > blue_cubes:
            return False
    return True

def min_cubes_needed(game):
    red_min = max(round[0] for round in game[1])
    green_min = max(round[1] for round in game[1])
    blue_min = max(round[2] for round in game[1])
    return red_min, green_min, blue_min

def main():
    """
    Main function
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--example', action='store_true')
    args = parser.parse_args()

    data_file = 'day02_example.dat' if args.example else 'day02.dat'

    part1_total = 0
    part2_total = 0
    with open(data_file, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            game = parse_game_data(line)
            if is_game_possible(game, 12, 13, 14):
                part1_total += game[0]

            red_min, green_min, blue_min = min_cubes_needed(game)
            part2_total += red_min * green_min * blue_min

    print(f"Answer (Part 1): {part1_total}")
    print(f"Answer (Part 2): {part2_total}")

if __name__ == "__main__":
    main()
