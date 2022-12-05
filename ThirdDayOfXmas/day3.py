import string

rucksacks_training = open(
    "thirddayofxmas/day3-training-input.txt").read().split('\n')
rucksacks_test = open("thirddayofxmas/day3-test-input.txt").read().split('\n')


def total(rucksacks):

    def find_common_items(rucksack):
        nItems = len(rucksack)
        nItems_per_compartment = int(nItems/2)
        compartment1 = rucksack[:nItems_per_compartment]
        compartment2 = rucksack[nItems_per_compartment:]
        common_item = [x for x in compartment1 if x in compartment2][0]

        return common_item

    common_items = []
    for r in rucksacks:
        common_item = find_common_items(r)
        common_items.append(common_item)

    alphabet = string.ascii_lowercase + string.ascii_uppercase
    priorities = [alphabet.index(x)+1 for x in alphabet]

    priority_list = []
    nLetters = len(alphabet)
    for item in common_items:
        for i in range(nLetters):
            if alphabet[i] == item:
                priority_list.append(priorities[i])

    Total = sum(priority_list)

    return Total


def total_grouped(rucksacks):

    def find_common_items_between_groups(rucksack_group):
        rucksack1 = rucksack_group[0]
        rucksack2 = rucksack_group[1]
        rucksack3 = rucksack_group[2]
        common_item = set(rucksack1).intersection(rucksack2, rucksack3)

        return common_item

    N = 3
    rucksack_groups = [rucksacks[n:n+N] for n in range(0, len(rucksacks), N)]

    common_items = []
    for r in rucksack_groups:
        common_item = find_common_items_between_groups(r)
        common_items.append(common_item)

    alphabet = string.ascii_lowercase + string.ascii_uppercase
    priorities = [alphabet.index(x)+1 for x in alphabet]

    priority_list = []
    nLetters = len(alphabet)
    for item in common_items:
        for ite in item:
            for i in range(nLetters):
                if alphabet[i] == ite:
                    priority_list.append(priorities[i])

    Total = sum(priority_list)

    return Total


total(rucksacks_training)

total(rucksacks_test)

'''
PART 2: 
We want to find the same common item 
but instead of between half of one rucksack its between three rucksacks
'''


total_grouped(rucksacks_training)

total_grouped(rucksacks_test)
