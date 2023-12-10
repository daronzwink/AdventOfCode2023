#!/usr/bin/env python3

import argparse


def main():
    """
    Main function
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--example', action='store_true')
    args = parser.parse_args()

    data_file = 'day06_example.dat' if args.example else 'day06.dat'

    races = []

    with open(data_file, 'r', encoding='utf-8') as file:
        time_data = []
        distance_data = []
        for line in file:
            words = line.split()
            if words[0] == "Time:":
                time_data = list(map(int, words[1:]))
            elif words[0] == "Distance:":
                distance_data = list(map(int, words[1:]))
                for i in range(len(time_data)):
                    races.append({"time": time_data[i], "distance": distance_data[i]})
                time_data = []
                distance_data = []

    part1_answer = 1
    for race in races:
        ways_to_win = 0
        for button_time in range(race['time']):
            distance = button_time * (race['time'] - button_time)
            if distance > race['distance']:
                ways_to_win += 1
        part1_answer *= ways_to_win

    print(f"Answer (Part 1): {part1_answer}")

    # Part 2
    races = []
    with open(data_file, 'r', encoding='utf-8') as file:
        time_data = ""
        distance_data = ""
        for line in file:
            words = line.split()
            if words[0] == "Time:":
                time_data = int("".join(words[1:]))
            elif words[0] == "Distance:":
                distance_data = int("".join(words[1:]))
                races.append({"time": time_data, "distance": distance_data})
                time_data = ""
                distance_data = ""

    part2_answer = 0
    for race in races:
        ways_to_win = 0
        for button_time in range(race['time']):
            distance = button_time * (race['time'] - button_time)
            if distance > race['distance']:
                ways_to_win += 1
        part2_answer = ways_to_win

    print(f"Answer (Part 2): {part2_answer}")

if __name__ == "__main__":
    main()
