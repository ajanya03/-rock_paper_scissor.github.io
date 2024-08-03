import random

guesses = ['rock','paper', 'scissor']

def who_wins(player, opponent):
    if player == 'paper' and opponent == 'scissor' or player == 'scissor' and opponent == 'paper' or player == 'rock' and opponent == 'scissor':
        print("You Won !!! . Computer Lose !!!")
    elif player == opponent:
        print("It's a TIE !!!")
    else:
        print("Computer Won!!! . You lose!!!")


def rock_paper_scissor():

    while True:
        user_input = input("Enter 1 to play 0 to quit : ")
        if user_input == '0':
            print("We are sorry to see you leave!!!")
            break
        else:
            # p > r , s > p , r > s
            player = input("Enter rock/paper/scissor to begin : ").lower()
            opponent = random.choice(guesses)
            print(f"Computer chooses {opponent}")
            who_wins(player, opponent)


rock_paper_scissor()