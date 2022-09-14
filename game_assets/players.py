import random

class Player_Base:
    def __init__(self):
        self._name = None
        self._credits = 0
        self._hand = []
        self._in_game = True

        self.create()
    
    def create(self):
        first_names = ["Brittney", "Curtis", "Lucas", "Chip", "Simon"]
        last_names = ["Moriah", "Tristin", "Troy", "Gale", "Lynn"]
        self._name = f"{random.choice(first_names)} {random.choice(last_names)}"

        self._credits = random.randint(10, 100)

    @property
    def full_name(self):
        return self._name

    @property
    def credits(self):
        return self._credits

    def draw_card(self, deck):
        print(f"{self.full_name} draws a card")

        my_new_card = deck.give_card()
        # print(f"My new card is: {my_new_card}")
        self._hand.append(my_new_card)

    def show_hand(self):
        print(self._hand)

    def __str__(self) -> str:
        return f"{self._name}"

    def __repr__(self) -> str:
        return f"{self._name}"

class Player(Player_Base):
    # overrides create() from base class
    def create(self):
        # runs base class create()
        super().create()
        self._name = input("What is your  name?")

class AIPlayer(Player_Base): 
    pass


# testing players
if __name__ == "__main__":
    from cards import Deck
    deck = Deck()

    ai_player = AIPlayer()
    ai_player.draw_card(deck)
    ai_player.draw_card(deck)
    ai_player.draw_card(deck)
    ai_player.draw_card(deck)
    ai_player.draw_card(deck)
    ai_player.show_hand()