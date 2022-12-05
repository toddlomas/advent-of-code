def calculate_order_9000(dataset, N, drawing_lines):
    input = open(
        f"fifthdayofxmas/day5-{dataset}-input.txt").read().split('\n\n')
    drawing = input[0].split('\n')

    stacks = [[] for _ in range(N)]
    for i in range(drawing_lines):
        line = drawing[i]
        crates = line[1::4]
        for s in range(len(crates)):
            if crates[s] != " ":
                stacks[s].append(crates[s])

    # Reverse all stacks
    stacks = [stack[::-1] for stack in stacks]

    for line in input[1].split("\n"):
        tokens = line.split(" ")
        n, src, dst = map(int, [tokens[1], tokens[3], tokens[5]])
        src -= 1
        dst -= 1

        for _ in range(n):
            pop = stacks[src].pop()
            stacks[dst].append(pop)

    tops = [stack[-1] for stack in stacks]
    order = "".join(tops)

    return order


calculate_order_9000("training", 3, 3)
calculate_order_9000("test", 9, 8)


'''
PART 2: CrateMover 9001
'''


def calculate_order_9001(dataset, N, drawing_lines):
    input = open(
        f"fifthdayofxmas/day5-{dataset}-input.txt").read().split('\n\n')
    drawing = input[0].split('\n')

    stacks = [[] for _ in range(N)]
    for i in range(drawing_lines):
        line = drawing[i]
        crates = line[1::4]
        for s in range(len(crates)):
            if crates[s] != " ":
                stacks[s].append(crates[s])

    # Reverse all stacks
    stacks = [stack[::-1] for stack in stacks]

    for line in input[1].split("\n"):
        tokens = line.split(" ")
        n, src, dst = map(int, [tokens[1], tokens[3], tokens[5]])
        src -= 1
        dst -= 1

        stacks[dst].extend(stacks[src][-n:])
        stacks[src] = stacks[src][:-n]

    tops = [stack[-1] for stack in stacks]
    order = "".join(tops)

    return order


calculate_order_9001("training", 3, 3)
calculate_order_9001("test", 9, 8)
