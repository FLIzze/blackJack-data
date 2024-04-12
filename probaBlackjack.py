import csv
import random

class Deck: 
    def __init__(self, nmb_player: int, nmb_deck: int = 1):
        self.deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10', 'A'] * 4 * nmb_deck
        self.players = [Player('Player'+str(i+1)) for i in range (nmb_player)]
        self.dealer = Player('Dealer')

    def shuffle(self):
        random.shuffle(self.deck)

    def start_game(self):
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
        self.choices = []
        self.name = name
        self.card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': [1, 11]}
        self.win = 1

    def get_nmb_card(self) -> int:
        total = 0
        ace_count = 0
        
        for card in self.cards:
            if card != 'A':
                total += self.card_values[card]
            else:
                ace_count += 1
        
        for _ in range(ace_count):
            if total + 11 <= 21:
                total += 11
            else:
                total += 1
        
        while total > 21 and ace_count > 0:
            total -= 10
            ace_count -= 1
        
        return total
    
    def get_start_cards(self, deck: list):
        self.cards.append(deck[0])
        deck.pop(0)

    def dealer_choice(self, deck: list):
        nmb_cards = self.get_nmb_card()
        if nmb_cards < 17:
            self.hit(deck)
            self.dealer_choice(deck)
        else:
            return
        
    def player_choice(self, deck: list):
        sys_random = random.SystemRandom()
        random_number = sys_random.randint(1, 6)
        get_nmb_cards = self.get_nmb_card()
        if get_nmb_cards > 21:
            self.choices.append('busted')
        elif get_nmb_cards == 21:
            if len(self.choices) == 0:
                self.choices.append('blackjack')
            else:
                self.choices.append('best hand')
        elif random_number < 2:
            self.hit(deck)
            self.player_choice(deck)
        elif random_number < 4:
            self.double(deck)
            self.player_choice(deck)
        else:
            self.choices.append('stay')
            
    def double(self, deck: list):
        self.cards.append(deck[0])
        self.choices.append('double')
        deck.pop(0)

    def hit(self, deck: list):
        self.cards.append(deck[0])
        self.choices.append('hit')
        deck.pop(0)

    def split(self, deck: list):
        self.cards = [self.cards[0]]

with open('probabilities.csv', 'w', newline='') as file:
    fieldnames = ['PlayerCard1', 'PlayerCard2', 'DealerHand', 'PlayerWin', 'PlayerChoices']
    writer = csv.DictWriter(file, fieldnames=fieldnames) 
    writer.writeheader()
file.close()
            
for i in range(250_000):
    deck = Deck(5, 4)
    deck.shuffle()
    deck.start_game()
    in_game = False

    for player in deck.players: 
        player.player_choice(deck.deck)

    for player in deck.players:
        if player.win == 1:
            in_game = True 

    if in_game:
        deck.dealer.dealer_choice(deck.deck)

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

    with open('probabilities.csv', 'a', newline='') as file:
        fieldnames = ['PlayerCard1', 'PlayerCard2', 'DealerHand', 'PlayerWin', 'PlayerChoices']
        writer = csv.DictWriter(file, fieldnames=fieldnames) 
        for player in deck.players:
            writer.writerow({'PlayerCard1': player.cards[0], 'PlayerCard2': player.cards[1], 'DealerHand': deck.dealer.cards[0], 'PlayerWin': player.win,  'PlayerChoices': player.choices[0]})
