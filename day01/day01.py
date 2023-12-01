#!/usr/bin/env python3

import re
import argparse

def main():
    """
    Main function
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--example', action='store_true')
    args = parser.parse_args()

    data_file_part1 = 'day01_example_part1.dat' if args.example else 'day01.dat'
    data_file_part2 = 'day01_example_part2.dat' if args.example else 'day01.dat'

    digit_map = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    part1_answer = 0
    part2_answer = 0

    # Process Data to get part 1 answer
    with open(data_file_part1, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()

            # Get Part 1 Answer
            part1_first_digit = re.search('\d', line).group()
            part1_last_digit = re.search('\d(?=\D*$)', line).group()
            part1_answer += int(part1_first_digit + part1_last_digit)

    # Process Data to get part 2 answer
    with open(data_file_part2, 'r', encoding='utf-8') as file:
        for line in file:

            line = line.strip()

            # Get Part 2 Digits
            part2_digits = []
            line_length = len(line)

            # Loop through each character in the line
            for i in range(line_length):

                # Analyze line to the character i and the remaining characters
                analyze_line = line[i:]

                # Get the first character
                if analyze_line[0].isdigit():
                    part2_digits.append(analyze_line[0])
                else:
                    # Check to see if the first part of the is a digit phrase
                    for key, value in digit_map.items():
                        if analyze_line.startswith(key):
                            part2_digits.append(value)
                            break

            # Get Part 2 Answer
            part2_first_digit = part2_digits[0]
            part2_last_digit = part2_digits[-1]
            part2_answer += int(str(part2_first_digit) + str(part2_last_digit))

    # Print Answers
    print(f"Answer (Part 1): {part1_answer}")
    print(f"Answer (Part 2): {part2_answer}")

if __name__ == "__main__":
    main()
