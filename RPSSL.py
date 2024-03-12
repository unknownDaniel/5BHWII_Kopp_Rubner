
import random
import json

def rules(wahl_spieler, wahl_computer):
    spielregeln = {
        "Stone": ["Scissors", "Lizard"],
        "Paper": ["Stone", "Spock"],
        "Scissors": ["Paper", "Lizard"],
        "Lizard": ["Paper", "Spock"],
        "Spock": ["Stone", "Scissors"]
    }

    if wahl_spieler == wahl_computer:
        return "draw"
    elif wahl_spieler in spielregeln[wahl_computer]:
        return "you win"
    else:
        return "you lose"


symbols = ["Stone", "Scissors", "Paper", "Spock", "Lizard"]


def computer():
    return random.choice(symbols)


def player():
    print("choose your symbol")
    for i in symbols:
        print(f"{symbols.index(i)}: " + i)

    player_choice = int(input("Entry (0-4): "))    #Input standardmäßig Strings
    if 0 <= player_choice <= 4:
        return symbols[player_choice]

    else:
        print("Choose number between 1 and 5")
        player()


def play():

    while True:

        print("\nWhat would you like to do:")
        print("0: Play")
        print("1: Show Statistics")
        print("2: Exit")

        user_input = int(input("Enter a number from 0-2: "))

        if user_input == 0:
            num_games = int(input("How many times would you like to play: "))
            for _ in range(num_games):   #_ weil Wert der Variable hier nicht relevant
                playgame()
            print("Your games have been played.")
        elif user_input == 1:
            showstatistic()
        elif user_input == 2:
            print("You have successfully logged out.")
            exit()

        else:
            print("Invalid input. Please enter a number between 0 and 2.")



game_results = {"player": 0, "computer": 0, "draw": 0}
def playgame():

    global game_results


    game_results = load_results()

    player_choice = player()
    computer_choice = computer()

    print(f"You chose: {player_choice}")
    print(f"The Computer chose {computer_choice}")

    result = rules(player_choice, computer_choice)

    print(result)

    if result == "you won":

        game_results["player"] += 1
    elif result == "you lose":
        game_results["computer"] += 1
    elif result == "draw":
        game_results["draw"] += 1
    else:
        print("error")
    save_results()


    return result

def save_results():

    with open("results.json", "w") as file:
        json.dump(game_results, file)

def load_results():

    try:
        with open("results.json", "r") as file:
            loaded_results = json.load(file)
            return loaded_results
    except FileNotFoundError:
        return {"player": 0, "computer": 0, "draw": 0}





def showstatistic():

    current_results = load_results()
    print("Current Statistics: ")
    print(f"Player: {current_results['player']}")
    print(f"Computer: {current_results['computer']}")
    print(f"Draw: {current_results['draw']}")


if __name__ == "__main__":
    play()