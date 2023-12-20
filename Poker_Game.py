import random

# Suits definieren
suits = ["Herz", "Karo", "Pik", "Kreuz"]

# Liste alle Karten mit Suits
alle_Karten = [f"({suit}) {card}" for suit in suits for card in ["Ass", "Zwei", "drei", "vier", "fünf", "6", "7", "8", "9", "10", "B", "D", "K"]]

def poker(num_cards):
    deck = list(range(52))
    ziehungen = random.sample(deck, num_cards)

    return ziehungen

# 1 Paar
def is_pair(ziehungen):
    return any(ziehungen[i] % 13 == ziehungen[j] % 13 for i in range(len(ziehungen)) for j in range(i + 1, len(ziehungen)))

# 2 Paare
def has_two_pairs(ziehungen):
    num_cards = len(ziehungen)



    card_counts = {}
    for i in range(num_cards):
        card_value = ziehungen[i] % 13
        if card_value in card_counts:
            card_counts[card_value] += 1
        else:
            card_counts[card_value] = 1

    pair_count = 0

    for count in card_counts.values():
        if count == 2:
            pair_count += 1

    return pair_count == 2

# Drilling
def is_three_of_a_kind(ziehungen):
    num_cards = len(ziehungen)

    for i in range(num_cards):
        count = 1
        for j in range(num_cards):
            if i != j and ziehungen[i] % 13 == ziehungen[j] % 13:
                count += 1
        if count >= 3:
            return True

    return False


# Straße
def is_straight(ziehungen):
    num_cards = len(ziehungen)

    unique_values = set()

    for i in range(num_cards):
        card_value = ziehungen[i] % 13
        unique_values.add(card_value)


    if len(unique_values) == num_cards and (max(unique_values) - min(unique_values)) == num_cards - 1:
        return True

    return False


# Flush
def has_flush(ziehungen):
    num_cards = len(ziehungen)

    suit_counts = {"Herz": 0, "Karo": 0, "Pik": 0, "Kreuz": 0}
    for i in range(num_cards):
        card_suit = ziehungen[i] // 13
        suit_name = suits[card_suit]
        suit_counts[suit_name] += 1


    return any(count >= 5 for count in suit_counts.values())

# Full House
def has_full_house(ziehungen):
    return is_three_of_a_kind(ziehungen) and is_pair(ziehungen)

# Vierling
def has_four_of_a_kind(ziehungen):
    card_counts = [ziehungen.count(ziehung) for ziehung in ziehungen]
    return 4 in card_counts

# Straight Flush
def is_straight_flush(cards, alle_Karten):
    if has_flush(cards) and is_straight(cards, alle_Karten):
        return True
    return False

# Royal Flush
def is_royal_flush(cards, alle_Karten):
    royal_flush_cards = ["10", "B", "D", "K", "Ass"]

    if has_flush(cards) and all(card in cards for card in royal_flush_cards):
        return True
    return False

def check_combinations(player, ziehungen, alle_Karten):
    num_cards = len(ziehungen)
    card_names = [alle_Karten[zufallszahl] for zufallszahl in ziehungen]

    formatted_card_names = [f"{card.split()[1]} {card.split()[0]}" for card in card_names]

    print(f"Person {player}: Karten: {', '.join(formatted_card_names)}")


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

def poker_statistic():
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

if __name__ == '__main__':
    poker_statistic()

