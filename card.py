class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    @property
    def get_suit(self):
        return self.suit

    @property
    def get_suit_value(self):
        return self.rank.value

    @property
    def get_rank(self):
        return self.rank

    def show_card_details(self):
        return "{} of {}".format(self.rank, self.suit)

###
card1 = Card("Hearts", "Ace")
# card1 = Card()
print(card1.show_card_details())
# print(card1.get_suit_value())
