class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    @property
    def get_suit(self):
        return self.suit

    @property
    def get_rank(self):
        return self.rank

    def show_card_details(self):
        return "{} of {}".format(self.rank, self.suit)

###
card1 = Card("Hearts", "Ace")
print(card1.show_card_details())
