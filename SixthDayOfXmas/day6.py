from collections import Counter
datastream = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
datastream = open(
    "/Users/toddlomas/Documents/AdventOfCode/SixthDayOfXmas/day6-test-input.txt").read()


def part_1(input):
    for i in range(3, len(input)-3):
        attempt = input[i-4:i]
        freq = Counter(attempt)
        if (len(freq) == 14):
            index = i
            break
    return i


part_1(datastream)


def part_2(input):
    for i in range(14, len(input)):
        attempt = input[i-14:i]
        freq = Counter(attempt)
        if (len(freq) == 14):
            index = i
            break
    return i


part_2(datastream)
