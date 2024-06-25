import random

ABBREVIATIONS = {
    'r': 'rock',
    'p': 'paper',
    's': 's',
    'l': 'lizard',
    'sp': 'spock'
}

VALID_CHOICES = list(ABBREVIATIONS.keys())

WINNING_COMBINATIONS = {
        "rock": ["scissors", "lizard"],
        "scissors": ["paper", "lizard"],
        "paper": ["rock", "spock"],
        "lizard": ["spock", "paper"],
        "spock": ["scissors", "rock"]
    }

def prompt(message):
    print(f"==> {message}")

def get_full_choice(abbr):
    return ABBREVIATIONS[abbr]

def is_player_winner(player, computer):
    player_full = get_full_choice(player)
    computer_full = get_full_choice(computer)
    return computer_full in WINNING_COMBINATIONS[player_full]

def display_winner(player, computer):
    player_full = get_full_choice(player)
    computer_full = get_full_choice(computer)
    prompt(f"You chose {player_full}, computer chose {computer_full}")

    if player_full == computer_full:
        prompt("It's a tie!")
    elif computer_full in WINNING_COMBINATIONS[player_full]:
        prompt("You win!")
    else:
        prompt("Computer wins!")

def display_scores(player_wins, computer_wins):
    prompt(f"Score - You: {player_wins}, Computer: {computer_wins}")

PLAYER_WINS = 0
COMPUTER_WINS = 0
WINNING_SCORE = 3

while True:
    prompt('Choose one (r: rock, p: paper, s: scissors, l: lizard, sp: spock):')
    choice = input().lower()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice. Use r, p, s, l, or sp.")
        choice = input().lower()

    computer_choice = random.choice(VALID_CHOICES)

    display_winner(choice, computer_choice)

    if choice != computer_choice:
        if is_player_winner(choice, computer_choice):
            PLAYER_WINS+= 1
        else:
            COMPUTER_WINS += 1

    display_scores(PLAYER_WINS, COMPUTER_WINS)

    prompt("Do you want to play again (y/n)?")
    answer = input().lower()
    while answer == '' or (answer[0] != 'n' and answer[0] != 'y'):
        prompt('Please enter "y" or "n".')
        answer = input().lower()

    if answer[0] != "y":
        break
