from random import randint

# Move list
moves = ['rock', 'paper', 'scissors', 'stop']
proper_moves = ['rock', 'paper', 'scissors']


def new_move(score=0):
    def lose_game():
        print("\nWould you like to play again?")
        again = input("Yes/No: ")
        if again.__contains__("yes"):
            new_move(0)
        if again.__contains__("no"):
            exit()
        else:
            print("\nThat's not a correct choice!")
            lose_game()

    # New move
    player_choice_text = input("\nChoose your move: ")

    # Converting computer choices to text
    computer_choice_int = randint(0, 2)
    computer_choice_text = moves[computer_choice_int]

    # Check for stop command
    if player_choice_text.__contains__("stop"):
        print("\nYou stopped the game! \nYour score was", score)
        lose_game()

    # Converting player choices to integers
    if player_choice_text.__contains__("rock"):
        player_choice_int = 0
    if player_choice_text.__contains__("paper"):
        player_choice_int = 1
    if player_choice_text.__contains__("scissors"):
        player_choice_int = 2

    # Player answer check
    while player_choice_text not in moves:
        print("\nThat's not a correct choice!")
        new_move(score+0)

    # Printing choices
    if player_choice_text in proper_moves:
        print("\nYou chose", player_choice_text, "\nThe computer chose", computer_choice_text)

    # Ties
    if player_choice_int == computer_choice_int:
        print("It's a tie!")
        new_move(score+0)

    # Wins
    if player_choice_int == 0 and computer_choice_int == 2:
        print("You won!")
        new_move(score+1)
    if player_choice_int == 1 and computer_choice_int == 0:
        print("You won!")
        new_move(score+1)
    if player_choice_int == 2 and computer_choice_int == 1:
        print("You won!")
        new_move(score+1)

    # Loses
    if player_choice_int == 0 and computer_choice_int == 1:
        print("You lost!")
        print("Score:", score)
        lose_game()
    if player_choice_int == 1 and computer_choice_int == 2:
        print("You lost!")
        print("Score:", score)
        lose_game()
    if player_choice_int == 2 and computer_choice_int == 0:
        print("You lost!")
        print("Score:", score)
        lose_game()


# Game intro
print("\nWelcome to a game of Rock, Paper, Scissors! \n\nThis is a simple script that will randomly choose a response"
      " and tell you if you've won. \nYou gain points by winning, and the game will end when you lose!")
print("\nEnter your move by typing it out and pressing the enter key. "
      "\nStop at any time by typing 'stop', to see your score and end the game.")
new_move()
