import re
training = open("fourthdayofxmas/day4-training-input.txt").read().split('\n')
test = open("fourthdayofxmas/day4-test-input.txt").read().split('\n')


def convert_range(range):
    return [int(x) for x in range]


def check_overlap(range_1, range_2):

    converted_range_1 = convert_range(range_1)
    converted_range_2 = convert_range(range_2)

    if converted_range_1[0] <= converted_range_2[0] <= converted_range_1[1]:
        if converted_range_1[0] <= converted_range_2[1] <= converted_range_1[1]:
            overlap = 1

        elif converted_range_2[0] <= converted_range_1[0] <= converted_range_2[1]:
            if converted_range_2[0] <= converted_range_1[1] <= converted_range_2[1]:
                overlap = 1
            else:
                overlap = 0
        else:
            overlap = 0
    elif converted_range_2[0] <= converted_range_1[0] <= converted_range_2[1]:
        if converted_range_2[0] <= converted_range_1[1] <= converted_range_2[1]:
            overlap = 1
        else:
            overlap = 0
    else:
        overlap = 0

    return overlap


def check_total_overlap(range_1, range_2):

    converted_range_1 = convert_range(range_1)
    converted_range_2 = convert_range(range_2)

    if converted_range_1[0] <= converted_range_2[0] <= converted_range_1[1]:
        overlap = 1
    elif converted_range_2[0] <= converted_range_1[0] <= converted_range_2[1]:
        overlap = 1
    else:
        overlap = 0

    return overlap


def main():
    count_part1 = 0
    count_part2 = 0
    for pair in test:
        individuals = pair.split(',')
        range_of_first_pair = re.findall(r'\d+', individuals[0])
        range_of_second_pair = re.findall(r'\d+', individuals[1])

        if check_overlap(range_of_first_pair, range_of_second_pair) == 1:
            count_part1 += 1

        if check_total_overlap(range_of_first_pair, range_of_second_pair) == 1:
            count_part2 += 1
    return print(f'Part 1: {count_part1} \nPart 2: {count_part2}')


if __name__ == "__main__":
    main()
