import random

class Deck:
        def __init__(self):
            self.cards = []

        @property
        def get_card(self):
            return self.cards

        def count_cards(self):
            return len(self.cards)

        def add_card(self, card):
            self.cards += card

        def add_52_cards(self):
            for suit_item in suit:
                for rank_item in rank:
                    card = Card(suit_item, rank_item)
                    self.cards += card

        def shuffle():
            random.shuffle(this.cards)

        def remove_card(card):
            self.cards.remove(card)

deck1 = Deck()
print(deck1.cards)
deck1.add_card(["5 of Hearts"])
print(deck1.cards)
