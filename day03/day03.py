#!/usr/bin/env python3

import argparse

def is_special_character(schematic, row, column):
    """
    Identifies if the given coordinate is a special character
    """
    return not schematic[row][column].isdigit() and schematic[row][column] not in ['.', ' ']

def main():
    """
    Main function
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--example', action='store_true')
    args = parser.parse_args()

    data_file = 'day03_example.dat' if args.example else 'day03.dat'

    part1_total = 0
    part2_total = 0
    with open(data_file, 'r', encoding='utf-8') as file:

        # Read in the data
        schematic = [list(line.strip()) for line in file]
        number_locations = []
        adjacent_numbers = []

        # Find all numbers in the schematic and their locations then add them to a list
        for row, _ in enumerate(schematic):
            for col, _ in enumerate(schematic[row]):

                # Get list of numbers found in the schematic
                if schematic[row][col].isdigit():
                    # This may be the beginning of a number, check to see if there are additional digits to the right and then set the column to the end of the number

                    # Get the end column of the number
                    end_col = col
                    while end_col < len(schematic[row]) and schematic[row][end_col].isdigit():
                        end_col += 1

                    full_number = int(''.join(schematic[row][col:end_col]))

                    # Check to see if there is already a number in the list that overlaps with the current number
                    already_added = False
                    for number in number_locations:
                        # Check if the row is the same and there is an overlap in the columns
                        if number[0] == row and (number[1] <= col <= number[2] or number[1] <= end_col <= number[2]):
                            already_added = True
                            break

                    if not already_added:
                        # Append an object with the row, start column, end column, and number
                        number_locations.append((row, col, end_col, full_number))

        # Find all special characters in the schematic and their locations then find the adjacent numbers and add them to a list
        for row, _ in enumerate(schematic):
            for col, _ in enumerate(schematic[row]):
                if is_special_character(schematic, row, col):

                    character_adjacent_numbers = []

                    # Check to see if any numbers are adjacent to the special character
                    for i in range(row - 1, row + 2):
                        for j in range(col - 1, col + 2):
                            if i < 0 or j < 0 or i >= len(schematic) or j >= len(schematic[row]):
                                continue
                            if schematic[i][j].isdigit():

                                # Check to see if there are adjacent numbers to the current row and column
                                for number in number_locations:
                                    if number[0] == i and number[1] <= j <= number[2]:

                                        # Append the number to the list of adjacent numbers for this special character
                                        if schematic[row][col] == '*' and number not in character_adjacent_numbers:
                                            character_adjacent_numbers.append(number)

                                        # Append the number object to the list of adjacent numbers, if not already added
                                        if number not in adjacent_numbers:
                                            adjacent_numbers.append(number)

                    # If the special character is a '*', and it is adjacent to exactly 2 full numbers, multiply them together and add to the total to the part 2 total
                    if schematic[row][col] == '*' and len(character_adjacent_numbers) == 2:
                        part2_total += character_adjacent_numbers[0][3] * character_adjacent_numbers[1][3]

        # Add up all the adjacent numbers
        if adjacent_numbers:
            part1_total += sum([number[3] for number in adjacent_numbers])

    print(f"Answer (Part 1): {part1_total}")
    print(f"Answer (Part 2): {part2_total}")


if __name__ == "__main__":
    main()
