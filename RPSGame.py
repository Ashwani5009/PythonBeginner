import random


def getChoices():
    playerChoice = input("Enter a choice: ")
    options = ["rock", "paper", "scissors"]
    computerChoice = random.choice(options)

    choices = {"player": playerChoice, "computer": computerChoice}
    return choices


def winner(player, computer):
    print(f"You chose {player} , computer chose {computer}")
    if player == computer:
        return "It's a tie."
    elif player == "rock":
        if computer == "paper":
            return "You lost."
        else:
            return "You Won."
    elif player == "scissors":
        if computer == "rock":
            return "You lost."
        else:
            return "You Won."
    else:
        if computer == "rock":
            return "You Won."
        else:
            return "You Lost."


choices = getChoices()
print(winner(choices["player"], choices["computer"]))
