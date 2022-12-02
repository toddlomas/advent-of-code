# Import packages
import fileinput

# Data sets to use
training_data = 'day1_training.txt'
test_data = 'day1_test.txt'


def find_the_strongest_elf(dataset):
    # Import test data
    list_of_calories_raw = []
    for line in fileinput.input(files=dataset):
        if line == '\n':
            list_of_calories_raw.append(0)
        else:
            list_of_calories_raw.append(line)

    list_of_calories = []
    # Clean breaklines from numbers
    for i in range(len(list_of_calories_raw)):
        str = list_of_calories_raw[i]
        if str != 0:
            str_cleaned = str.replace('\n', '')
            list_of_calories.append(int(str_cleaned))
        else:
            list_of_calories.append(0)

    # Group Elves
    y = 0
    elven_groups = []
    nFood_items = len(list_of_calories)
    for num in list_of_calories:
        i = list_of_calories.index(num)
        if num != 0:
            y = y+num
            if i == nFood_items-1:
                elven_groups.append(y)
        else:
            elven_groups.append(y)
            y = 0

    # Who carries the most?
    strongest_elf = elven_groups.index(max(elven_groups)) + 1
    print(f'The elf with the biggest weight is: Elf Number {strongest_elf}')
    return strongest_elf


# Training data, expected answer is 4, attained answer is 4 ✅
find_the_strongest_elf(training_data)

# Test data
find_the_strongest_elf(test_data)

# ANSWER IS 88
