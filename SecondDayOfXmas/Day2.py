
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


def calculateScore(data):
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


calculateScore(training_data)  # Total is 15
calculateScore(test_data)  # Total is 12535


'''
Part 2
"X means you need to lose,
Y means you need to end the round in a draw,
Z means you need to win. Good luck!"

In the first round, your opponent will choose Rock (A), 
and you need the round to end in a draw (Y), so you also choose Rock. 
This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B), 
and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
    "1": "Rock",
    "2": "Paper",
    "3": "Scissors",
    "0": "Lose",
    "3": "Draw",
    "6": "Win",

'''

ref = {
    "X": "Lose",
    "Y": "Draw",
    "Z": "Win",
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors"
}


'''    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",'''


def calculateScore2ndRound(data):
    score = 0
    for game in data:
        print(game)
        letter = game[0]
        ldw = ref[game[1]]
        print(f'Choice : {ref[letter]}')
        print(f'Result needs to be: {ldw}')
        if letter == 'A':
            if ldw == "Win":
                print("Paper beats Rock")
                score += 8
            elif ldw == "Draw":
                print("Rock draws Rock")
                score += 4
            elif ldw == "Lose":
                print("Scissors Loses Rock")
                score += 3
        elif letter == 'B':
            if ldw == "Win":
                print("Scissors beats Paper")
                score += 9
            elif ldw == "Draw":
                print("Paper draws paper")
                score += 5
            elif ldw == "Lose":
                print("Rock loses Paper")
                score += 1
        elif letter == 'C':
            if ldw == "Win":
                print("Rock wins Scissors")
                score += 7
            elif ldw == "Draw":
                print("Scissors draw Scissors")
                score += 6
            elif ldw == "Lose":
                print("Paper loses Scissors")
                score += 2

    print(f'Total score is: {score}')
    return score


calculateScore2ndRound(training_data)  # Total is 12
calculateScore2ndRound(test_data)  # Total is 15457
