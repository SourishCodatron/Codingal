import random
from colorama import init, Fore
init(autoreset=True)

ROCK = 0
PAPER = 1
SCISSORS = 2

moves = ["rock", "paper", "scissors"]

win_conditions = [
    (ROCK, SCISSORS),
    (PAPER, ROCK),
    (SCISSORS, PAPER),
]


def ai_move():
    choice = random.choice(moves)
    print(Fore.YELLOW + f"AI: {choice}")
    return moves.index(choice)


def player_move():
    while True:
        choice = input(Fore.CYAN + "Enter move: ").strip().lower()

        if choice in moves:
            return moves.index(choice)
        else:
            print(Fore.RED + "ENTER THE CORRECT WORD")


def check_win(player, ai):
    if player == ai:
        return "tie"

    if (player, ai) in win_conditions:
        return "player"
    return "ai"


def score(player_score, ai_score, result):
    if result == "tie":
        print("It's a tie")
    elif result == "player":
        player_score += 1
        print("You get one point")
    else:
        ai_score += 1
        print("AI gets one point")

    return player_score, ai_score


def rules():
    print(Fore.GREEN + "Play rock, paper, or scissors")
    print(Fore.GREEN + "You will play against an AI")
    print(Fore.GREEN + "The maximum points are 5")


def max_points(player_score, ai_score):
    if player_score == 5:
        print("You win")
        return True

    if ai_score == 5:
        print("AI wins")
        return True

    return False

def rock_paper_scissors():
    print("Welcome to Rock-Paper-Scissors!")
    player_name = input(Fore.GREEN + "Enter your name: ").strip()
    if not player_name:
        player_name = "Player"

    player_score = 0
    ai_score = 0
    
    rules()
    
    while True:
        player_choice = player_move()
        ai_choice = ai_move()

        result = check_win(player_choice, ai_choice)
        player_score, ai_score = score(player_score, ai_score, result)

        print(f"Player's score:  {player_score}")
        print(f"Ai's score: {ai_score}")

        if max_points(player_score, ai_score):
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        rock_paper_scissors()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    rock_paper_scissors()
