class Player:
    def __init__(self, name):
        self._name = name
        self._hand = []
        self._score = 0

    @property
    def get_name(self):
        return self._name

    @property
    def get_score(self):
        return self._score

    @property
    def get_hand(self):
        return self._hand

    def count_cards(self):
        return len(self._hand)

    def take_card(self, card):
        self._hand.append(card)

    def get_score(self):
        return self._score

    def add_points_to_score(self, card):
        self._score += card.rank

    def remove_card(self, card):
        self._hand.remove(card)

    def remove_all_cards(self):
        while self._hand > 0:
            self._hand.pop()

player1 = Player("Banjo")
# print(player1.name)
print(player1.get_name)
print(player1.get_hand)
print(player1.get_score())
#I want to find out more about how Python deals with getters and setters.
