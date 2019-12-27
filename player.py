class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.score = 0

    @property
    def get_name(self):
        return self.name

    @property
    def get_score(self):
        return self.score

    @property
    def get_hand(self):
        return self.hand

    def count_cards(self):
        return len(self.hand)

    def take_card(sel, card):
        self.hand.append(card)

    def get_score(self):
        return self.score

    def add_points_to_score(self, card):
        self.score += card.rank

    def remove_card(self, card):
        self.hand.remove(card)

    def remove_all_cards(self):
        while self.hand > 0:
            self.hand.pop()

player1 = Player("Banjo")
print(player1.get_name())
