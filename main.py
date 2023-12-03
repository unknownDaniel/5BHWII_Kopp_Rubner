import random

# Define the suits
suits = ["♥", "♦", "♠", "♣"]

# Create a list of all cards with suits
alle_Karten = [f"({suit}) {card}" for suit in suits for card in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "B", "D", "K", "Ass"]]


def poker(num_cards):
    deck = list(range(52))  # Create a deck of cards (52 integers)
    ziehungen = random.sample(deck, num_cards)  # Draw random cards from the deck

    return ziehungen

#ein Paar
def is_pair(ziehungen):
    return any(ziehungen[i] % 13 == ziehungen[j] % 13 for i in range(len(ziehungen)) for j in range(i + 1, len(ziehungen)))

#2 paare
def has_two_pairs(ziehungen):
    num_cards = len(ziehungen)

    # Erstellen Sie eine Zählung der Kartenwerte
    card_counts = {}
    for i in range(num_cards):
        card_value = ziehungen[i] % 13
        if card_value in card_counts:
            card_counts[card_value] += 1
        else:
            card_counts[card_value] = 1

    pair_count = 0  # Zählen Sie die Anzahl der Paare

    for count in card_counts.values():
        if count == 2:
            pair_count += 1

    return pair_count == 2  # Es gibt zwei Paare

#Drilling
def is_three_of_a_kind(ziehungen):
    num_cards = len(ziehungen)

    for i in range(num_cards):
        count = 1  # Zähler für Karten mit demselben Wert, beginnend mit 1
        for j in range(num_cards):
            if i != j and ziehungen[i] % 13 == ziehungen[j] % 13:
                count += 1
        if count >= 3:
            return True  # Ein Drilling wurde gefunden

    return False  # Kein Drilling gefunden


#Straße
def is_straight(ziehungen):
    num_cards = len(ziehungen)

    # Erstellen Sie eine Menge, um eindeutige Werte zu speichern
    unique_values = set()

    for i in range(num_cards):
        card_value = ziehungen[i] % 13
        unique_values.add(card_value)

    # Überprüfen Sie, ob die Anzahl der eindeutigen Werte gleich der Anzahl der gezogenen Karten ist
    # und ob die Differenz zwischen dem maximalen und minimalen Wert gleich der Anzahl der Karten - 1 ist
    if len(unique_values) == num_cards and (max(unique_values) - min(unique_values)) == num_cards - 1:
        return True  # Eine Straße wurde gefunden

    return False  # Keine Straße gefunden


#Flush
def has_flush(ziehungen):
    num_cards = len(ziehungen)

    # Erstellen Sie eine Zählung der Farben
    suit_counts = {"♥": 0, "♦": 0, "♠": 0, "♣": 0}
    for i in range(num_cards):
        card_suit = ziehungen[i] // 13
        suit_name = suits[card_suit]
        suit_counts[suit_name] += 1

    # Überprüfen, ob eine der Farben fünf Karten hat
    return any(count >= 5 for count in suit_counts.values())

#FUll House
def has_full_house(ziehungen):
    return is_three_of_a_kind(ziehungen) and is_pair(ziehungen)

#Vierling
def has_four_of_a_kind(ziehungen):
    card_counts = [ziehungen.count(ziehung) for ziehung in ziehungen]
    return 4 in card_counts

#Straight Flush
def is_straight_flush(cards, alle_Karten):
    if has_flush(cards) and is_straight(cards, alle_Karten):
        return True
    return False

#Royal Flush
def is_royal_flush(cards, alle_Karten):
    royal_flush_cards = ["10", "B", "D", "K", "Ass"]

    if has_flush(cards) and all(card in cards for card in royal_flush_cards):
        return True
    return False



def colored_symbol(symbol, color):
    color_mapping = {
        '♦': 'rot',  # Herz-Symbol in Rot
        '♣': 'schwarz',  # Pik-Symbol in Schwarz
        '♠': 'schwarz',  # Pik-Symbol in Schwarz
        '♥': 'rot',  # Herz-Symbol in Rot
        # Fügen Sie hier weitere Symbole und Farben hinzu, wenn nötig.
    }

    reset_color = '\033[0m'  # Reset color to default

    if symbol in color_mapping:
        symbol_text = color_mapping[symbol]
        return f"\033[91m{symbol}\033[0m ({symbol_text})"  # Das Symbol wird rot oder schwarz mit der zugehörigen Farbbezeichnung
    return symbol
def check_combinations(player, ziehungen, alle_Karten):
    num_cards = len(ziehungen)
    card_names = [alle_Karten[zufallszahl] for zufallszahl in ziehungen]

    formatted_card_names = [f"{colored_symbol(card.split()[1], card.split()[0])} {card.split()[0]}" for card in card_names]

    def sort_by_card_value(card):
        card_values = [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "B", "D", "K", "Ass"]
        return card_values.index(card.split()[0])

    formatted_card_names.sort(key=sort_by_card_value)

    print(f"Person {player}: Karten: {', '.join(formatted_card_names)}")

    # Check for various hand combinations
    if is_royal_flush(ziehungen, alle_Karten):
        print(f"Person {player} hat einen Royal Flush.")
    elif is_straight_flush(ziehungen, alle_Karten):
        print(f"Person {player} hat einen Straight Flush.")
    elif has_four_of_a_kind(ziehungen):
        print(f"Person {player} hat einen Vierling.")
    elif has_full_house(ziehungen):
        print(f"Person {player} hat ein Full House.")
    elif has_flush(ziehungen):
        print(f"Person {player} hat einen Flush.")
    elif is_straight(ziehungen):
        print(f"Person {player} hat eine Straße.")
    elif is_three_of_a_kind(ziehungen):
        print(f"Person {player} hat einen Drilling.")
    elif has_two_pairs(ziehungen):
        print(f"Person {player} hat zwei Paare.")
    elif is_pair(ziehungen):
        pairs = []
        card_values = [ziehung % 13 for ziehung in ziehungen]
        for value in set(card_values):
            if card_values.count(value) == 2:
                pairs.append(alle_Karten[ziehungen[card_values.index(value)]])
        print(f"Person {player} hat ein Paar aus: {', '.join(pairs)}.")
    else:
        print(f"Person {player} hat nur eine High Card.")

def poker_statistics():
    while True:
        try:
            num_players = int(input("Wie viele Spieler? (1-5, 0 zum Beenden): "))

            if num_players == 0:
                break
            elif num_players < 1 or num_players > 5:
                print("Bitte geben Sie eine Anzahl zwischen 1 und 5 ein.")
                continue
        except ValueError:
            print("Ungültige Eingabe. Bitte geben Sie eine Zahl zwischen 1 und 5 ein.")
            continue

        num_cards = 5

        for player in range(1, num_players + 1):
            gezogene_zahlen = poker(num_cards)
            check_combinations(player, gezogene_zahlen, alle_Karten)





def check_combinations(player, ziehungen, alle_Karten):
    num_cards = len(ziehungen)
    card_names = [alle_Karten[zufallszahl] for zufallszahl in ziehungen]

    formatted_card_names = [f"{colored_symbol(card.split()[1], card.split()[0])} {card.split()[0]}" for card in card_names]

    def sort_by_card_value(card):
        card_values = [ "2", "3", "4", "5", "6", "7", "8", "9", "10", "B", "D", "K", "Ass"]
        return card_values.index(card.split()[0])

    formatted_card_names.sort(key=sort_by_card_value)

    print(f"Person {player}: Karten: {', '.join(formatted_card_names)}")

    # Check for various hand combinations
    if is_royal_flush(ziehungen, alle_Karten):
        return "Royal Flush"
    elif is_straight_flush(ziehungen, alle_Karten):
        return "Straight Flush"
    elif has_four_of_a_kind(ziehungen):
        return "Four of a Kind"
    elif has_full_house(ziehungen):
        return "Full House"
    elif has_flush(ziehungen):
        return "Flush"
    elif is_straight(ziehungen):
        return "Straight"
    elif is_three_of_a_kind(ziehungen):
        return "Three of a Kind"
    elif has_two_pairs(ziehungen):
        return "Two Pairs"
    elif is_pair(ziehungen):
        return "One Pair"
    else:
        return "High Card"

def poker_statistics_percentage():
    num_games = 100000
    combinations_count = {
        "Royal Flush": 0,
        "Straight Flush": 0,
        "Four of a Kind": 0,
        "Full House": 0,
        "Flush": 0,
        "Straight": 0,
        "Three of a Kind": 0,
        "Two Pairs": 0,
        "One Pair": 0,
        "High Card": 0
    }

    for _ in range(num_games):
        gezogene_zahlen = poker(5)
        result = check_combinations(None, gezogene_zahlen, alle_Karten)
        combinations_count[result] += 1

    print("Kombinationen und deren prozentualer Anteil:")
    for combination, count in combinations_count.items():
        percentage = (count / num_games) * 100
        print(f"{combination}: {count} ({percentage:.2f}%)")

if __name__ == '__main__':
   poker_statistics()

