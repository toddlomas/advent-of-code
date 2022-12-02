# elves = open("day1_test.txt").read().split("\n\n")
# calories = [sum(map(int, elf.split())) for elf in elves]
# print(max(calories), sum(sorted(calories)[-3:]))

# Correct Solution

# Data sets to use
training_data = 'day1_training.txt'
test_data = 'day1_test.txt'


def find_the_strongest_elf(dataset):
    # Import test data
    elves = open(dataset).read().split("\n\n")

    list_of_calories_total_int = [sum(map(int, elf.split())) for elf in elves]

    # Who carries the most?
    strongest_elf_carries = max(list_of_calories_total_int)
    print(
        f'The elf with the biggest weight is carrying: {strongest_elf_carries}')
    return strongest_elf_carries


# Training data, expected answer is 24000, attained answer is 24000 ✅
find_the_strongest_elf(training_data)

# Test data
find_the_strongest_elf(test_data)

# ANSWER IS 72718
