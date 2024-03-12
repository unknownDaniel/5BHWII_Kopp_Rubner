# terminal --> in console schreiben
# comp vs player
# counter für Gewinner
# zähle alle gewählten Symbole
# write to file
# Consolenausgabe: Spielen, Statisik (Scanner)

import random
import json

def rules(wahl_spieler, wahl_computer):
    spielregeln = {
        "Stein": ["Schere", "Echse"],
        "Papier": ["Stein", "Spock"],
        "Schere": ["Papier", "Echse"],
        "Echse": ["Papier", "Spock"],
        "Spock": ["Stein", "Schere"]
    }

    if wahl_spieler == wahl_computer:
        return "Unentschieden!"
    elif wahl_spieler in spielregeln[wahl_computer]:
        return "Du gewinnst!"
    else:
        return "Du verlierst!"


symbols = ["Stein", "Schere", "Papier", "Spock", "Echse"]


def computer():
    return random.choice(symbols)


def player():
    # player_choice

    print("choose your symbol")
    for i in symbols:
        print(f"{symbols.index(i)}: " + i)

    player_choice = int(input("Ihre Eingabe (0-4): "))
    if 0 <= player_choice <= 4:
        return symbols[player_choice]

    else:
        print("Ungültige Eingabe. Bitte wählen Sie eine Zahl zwischen 1 und 5.")
        player()


def play():
    #game_results = {"player": 0, "computer": 0, "draw": 0}
    #global game_results
    #game_results = load_results()

    symbol_counts = {symbol: 0 for symbol in symbols}


    while True:

        print("\nWhat would you like to do:")
        print("0: Play")
        print("1: Show Statistics")
        print("2: Exit")

        user_input = int(input("Enter a number from 0-2: "))

        if user_input == 0:
            num_games = int(input("How many times would you like to play: "))
            for _ in range(num_games):
                playgame()
            print("Your games have been played.")
        elif user_input == 1:
            showstatistic()
        elif user_input == 2:
            print("You have successfully logged out.")

        else:
            print("Invalid input. Please enter a number between 0 and 2.")



game_results = {"player": 0, "computer": 0, "draw": 0}
def playgame():

    global game_results


    game_results = load_results()

    player_choice = player()
    computer_choice = computer()

    print(f"Du hast {player_choice} gewählt.")
    print(f"Der Computer hat {computer_choice} gewählt.")

    result = rules(player_choice, computer_choice)

    print(result)

    if result == "Du gewinnst!":
        # Spieler gewinnt, erhöhe den Counter um 1
        game_results["player"] += 1
    elif result == "Du verlierst!":
        game_results["computer"] += 1
    elif result == "Unentschieden!":
        game_results["draw"] += 1
    else:
        print("Fehler diesdas")
    save_results()


    return result

def save_results():
    # Speichere die Ergebnisse in einer JSON-Datei
    with open("results.json", "w") as file:
        json.dump(game_results, file)

def load_results():
    # Lade die Ergebnisse aus der JSON-Datei
    try:
        with open("results.json", "r") as file:
            loaded_results = json.load(file)
            return loaded_results
    except FileNotFoundError:
        return {"player": 0, "computer": 0, "draw": 0}





def showstatistic():
    # Gib die aktuellen Spielstatistiken aus
    current_results = load_results()
    print("Aktuelle Statistiken:")
    print(f"Spieler: {current_results['player']}")
    print(f"Computer: {current_results['computer']}")
    print(f"Unentschieden: {current_results['draw']}")


if __name__ == "__main__":
    play()