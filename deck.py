import random
from suit import Suit
from rank import Rank
from enum import Enum
from card import Card

# deck = []
# ranks = []
# def get_rank_list():
#     for card in Rank:
#         ranks.append({card.name: card.value})
#     return ranks
#
# def fill_deck():
#     for suit in Suit:
#         for rank in Rank:
#             deck.append({suit: rank})


class Deck:
        def __init__(self):
            self.cards = []

        @property
        def get_cards(self):
            return self.cards

        def count_cards(self):
            return len(self.cards)

        def add_card(self, card):
            self.cards.append(card)

        def add_52_cards(self):
            for suit_item in Suit:
                for rank_item in Rank:
                    card = Card(suit_item, rank_item)
                    self.cards.append(card)

        def shuffle(self):
            random.shuffle(self.cards)

        def remove_card(self, card):
            self.cards.remove(card)

        def show_card(self, card):
            card_details = self.cards[card]
            rank_value = card_details.rank.value
            suit_value = card_details.suit.value
            # return "{} of {}".format(card_details.rank, card_details.suit)
            return "{} of {}".format(rank_value, suit_value)

deck1 = Deck()
print(deck1.cards)
deck1.add_52_cards()
print(deck1.cards)
print(deck1.show_card(0))
# deck1.add_card({"Ace of Hearts"})
# deck1.add_card({"Two of Hearts"})
# deck1.add_card({"Three of Hearts"})
# deck1.add_card({"Four of Hearts"})
# deck1.add_card({"Five of Hearts"})
# deck1.add_card({"Six of Hearts"})
# print(deck1.cards)
print(deck1.count_cards())
# deck1.shuffle()
#If I run this multiple times, I expect the order to be different from the previous print
# print(deck1.cards)
#The add card method is not acting the way I expected. It works (adds one item) if I pass a list or dictionary as the argument, but if I pass a string it ads multiple items.
