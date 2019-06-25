import random

class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

class Deck:
    def __init__(self):
        self.card_set = []
        # self.num_of_cards = 52

    def populate_deck(self):
        suits = ["Heart", "Spade", "Club", "Diamond"]
        for suit in suits:
            for i in range(1, 14):
                if i == 1:
                    rank = "Ace"
                    value = [1, 10]
                elif i == 11:
                    rank = "Jack"
                    value = 10
                elif i == 12:
                    rank = "Queen"
                    value = 10
                elif i == 13:
                    rank = "King"
                    value = 10
                else:
                    rank = i
                    value = i
                card = Card(suit, rank, value)
                self.card_set.append(card)

    def pick_random_card(self):
        card = self.card_set.pop(random.randint(1, len(self.card_set)))
        # return len(self.card_set), card.suit, card.rank, card.value
        return card

    def shuffle():
        pass

class Game:
    def __init__(self):
        pass

    def win():
        pass

class Player:
    def __init__(self):
        # print("I pass")

    def hit():
        pass

    def stand():
        pass

class Dealer(Player):
    def __init__(self):
        super().__init__()

deck = Deck()
deck.populate_deck()
# print(deck.pick_random_card())
# print(deck.pick_random_card())
# print(deck.pick_random_card())
# print(deck.pick_random_card())
