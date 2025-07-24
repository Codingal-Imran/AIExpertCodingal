import random
choices = ['rock', 'paper', 'scissors']

def user_choice():
    choice = ''
    while choice not in choices:
        choice = input("Choose Rock, Paper, or Scissors: ").lower()
        if choice not in choices:
            print("Invalid choice, please try again.")
    return choice

def computer_choice():
    return random.choice(choices)

while True:
    user = user_choice()
    computer = computer_choice()
    print(f"Computer chose: {computer.capitalize()}")

    if user == computer:
        print("It's a tie!")
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        print("User wins!")
    else:
        print("Computer wins!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break