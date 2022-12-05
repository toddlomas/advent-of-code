import string

rucksacks_training = open(
    "thirddayofxmas/day3-training-input.txt").read().split('\n')
rucksacks_test = open("thirddayofxmas/day3-test-input.txt").read().split('\n')

rucksack = rucksacks_training
compartment1 = rucksack[:12]  # 'vJrwpWtwJgWr'
compartment2 = rucksack[12:]  # 'hcsFMMfFFhFp'


def total(rucksacks):

    def findCommonItems(rucksack):
        nItems = len(rucksack)
        nItemsPerCont = int(nItems/2)
        compartment1 = rucksack[:nItemsPerCont]
        compartment2 = rucksack[nItemsPerCont:]
        commonItem = [x for x in compartment1 if x in compartment2][0]

        return commonItem

    commonItems = []
    for r in rucksacks:
        commonItem = findCommonItems(r)
        commonItems.append(commonItem)

    alphabet = string.ascii_lowercase + string.ascii_uppercase
    priorities = [alphabet.index(x)+1 for x in alphabet]

    priority_list = []
    nLetters = len(alphabet)
    for item in commonItems:
        for i in range(nLetters):
            if alphabet[i] == item:
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


def totalGrouped(rucksacks):

    def findCommonItemsBetweenGroups(rucksackGroup):
        rucksack1 = rucksackGroup[0]
        rucksack2 = rucksackGroup[1]
        rucksack3 = rucksackGroup[2]
        commonItem = set(rucksack1).intersection(rucksack2, rucksack3)

        return commonItem

    N = 3
    rucksackGroups = [rucksacks[n:n+N] for n in range(0, len(rucksacks), N)]

    commonItems = []
    for r in rucksackGroups:
        commonItem = findCommonItemsBetweenGroups(r)
        commonItems.append(commonItem)

    alphabet = string.ascii_lowercase + string.ascii_uppercase
    priorities = [alphabet.index(x)+1 for x in alphabet]

    priority_list = []
    nLetters = len(alphabet)
    for item in commonItems:
        for ite in item:
            for i in range(nLetters):
                if alphabet[i] == ite:
                    priority_list.append(priorities[i])

    Total = sum(priority_list)

    return Total


totalGrouped(rucksacks_training)

totalGrouped(rucksacks_test)
