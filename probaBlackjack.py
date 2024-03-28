import random

class Deck: 
    def __init__(self, nmb_player: int):
        self.deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
        self.players = [Player('Player'+str(i+1)) for i in range (nmb_player)]
        self.dealer = Player('Dealer')

    def shuffle(self):
        random.shuffle(self.deck)

    def start_game(self):
        print(f'Starting game!\n{len(self.players)} players in game.')
        for _ in range(2):
            for player in self.players:
                player.get_start_cards(self.deck)
            self.dealer.get_start_cards(self.deck)
        self.dealer.get_nmb_card()
        for player in self.players:
            player.get_nmb_card()


class Player:
    def __init__(self, name: str):
        self.cards = []
        self.name = name
        self.card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        self.win = 1

    def get_nmb_card(self) -> int:
        nmb_cards = 0
        for card in self.cards:
           nmb_cards += self.card_values[card] 
        return nmb_cards
    
    def get_start_cards(self, deck: list):
        self.cards.append(deck[0])
        deck.pop(0)

    def hit(self, deck: list):
        self.cards.append(deck[0])
        # print(f"{self.name} hits a {deck[0]}")
        deck.pop(0)
        nmb_cards = self.get_nmb_card()
        if nmb_cards < 17:
            self.hit(deck)
        elif nmb_cards > 21:
            self.win = 0
        #     print(f'{self.name} busted.')
        # else:
        #     print(f'{self.name} stays.')
            
    def double(self, deck: list):
        self.cards.append(deck[0])
        deck.pop(0)

            

deck = Deck(2)
deck.shuffle()
deck.start_game()
in_game = False

#0 lost
#1 won
#2 pushed
for player in deck.players: 
    player.hit(deck.deck)
    print(f'{player.name}: {player.cards}: {player.get_nmb_card()}')

for player in deck.players:
    if player.win == 1:
        in_game = True 

if in_game:
    deck.dealer.hit(deck.deck)
print(f'{deck.dealer.name}: {deck.dealer.cards}: {deck.dealer.get_nmb_card()}')

for player in deck.players:
    playerNmb = player.get_nmb_card()
    dealerNmb = deck.dealer.get_nmb_card()
    if (playerNmb > dealerNmb and playerNmb <= 21):
        player.win = 1
    elif (playerNmb <= 21 and dealerNmb > 21):
        player.win = 1
    elif (playerNmb > 21):
        player.win = 0
    elif (playerNmb < dealerNmb and dealerNmb <= 21):
        player.win = 0
    elif (playerNmb == dealerNmb and dealerNmb <= 21):
        player.win = 2

for player in deck.players:
    print(player.get_nmb_card(), deck.dealer.get_nmb_card())
    if player.win == 0:
        print(f'{player.name}: lost')
    elif player.win == 1:
        print(f'{player.name}: won')
    else:
        print(f'{player.name}: pushed')