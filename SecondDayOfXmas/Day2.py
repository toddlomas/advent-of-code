training_data = open(
    "seconddayofxmas/strategy-guide-training.txt").read().split("\n")

test_data = open(
    "seconddayofxmas/strategy-guide-test.txt").read().split("\n")

training_data = [x.replace(" ", "") for x in training_data]
test_data = [x.replace(" ", "") for x in test_data]

ref = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors"
}


def calculate_score(data):
    score = 0
    for game in data:
        if game[1] == 'X':
            score += 1
        elif game[1] == 'Y':
            score += 2
        elif game[1] == 'Z':
            score += 3

        if game[0] == "A" and game[1] == "Y":
            score += 6

        elif game[0] == "B" and game[1] == "Z":
            score += 6

        elif game[0] == "C" and game[1] == "X":
            score += 6

        elif game[0] == "A" and game[1] == "X":
            score += 3

        elif game[0] == "B" and game[1] == "Y":
            score += 3

        elif game[0] == "C" and game[1] == "Z":
            score += 3

    print(f'Total score is: {score}')
    return score


calculate_score(training_data)  # Total is 15
calculate_score(test_data)  # Total is 12535

'''
PART 2
'''

ref = {
    "X": "Lose",
    "Y": "Draw",
    "Z": "Win",
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors"
}


def calculate_score_2nd_round(data):
    score = 0
    for game in data:
        letter = game[0]
        ldw = ref[game[1]]
        if letter == 'A':
            if ldw == "Win":
                score += 8
            elif ldw == "Draw":
                score += 4
            elif ldw == "Lose":
                score += 3
        elif letter == 'B':
            if ldw == "Win":
                score += 9
            elif ldw == "Draw":
                score += 5
            elif ldw == "Lose":
                score += 1
        elif letter == 'C':
            if ldw == "Win":
                score += 7
            elif ldw == "Draw":
                score += 6
            elif ldw == "Lose":
                score += 2

    print(f'Total score is: {score}')
    return score


calculate_score_2nd_round(training_data)  # Total is 12
calculate_score_2nd_round(test_data)  # Total is 15457
