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
            self.cards.append(card)

        def add_52_cards(self):
            for suit_item in suit:
                for rank_item in rank:
                    card = Card(suit_item, rank_item)
                    self.cards += card

        def shuffle(self):
            random.shuffle(self.cards)

        def remove_card(self, card):
            self.cards.remove(card)

deck1 = Deck()
print(deck1.cards)
deck1.add_card({"Ace of Hearts"})
deck1.add_card({"Two of Hearts"})
deck1.add_card({"Three of Hearts"})
deck1.add_card({"Four of Hearts"})
deck1.add_card({"Five of Hearts"})
deck1.add_card({"Six of Hearts"})
print(deck1.cards)
deck1.shuffle()
#If I run this multiple times, I expect the order to be different from the previous print
print(deck1.cards)
#The add card method is not acting the way I expected. It works (adds one item) if I pass a list or dictionary as the argument, but if I pass a string it ads multiple items.
