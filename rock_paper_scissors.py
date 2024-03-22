import random

options = ("rock", "paper", "scissors")
computer = random.choice(options)

while True:
    print("Press 'q' to quit")
    player = input("Enter a choice (rock, paper, scissors): ").lower()
    if player.lower() == "q":
        break
    elif player not in options:
        continue
    else:
        print("Player: {}".format(player))
        print("Computer: {}".format(computer))
        if player == computer:
            print("It's a tie!")
        elif player == "rock" and computer == "scissors":
            print("You win!")
        elif player == "paper" and computer == "rock":
            print("You win!")
        elif player == "scissors" and computer == "paper":
            print("You win!")
        else:
            print("You lose!")
