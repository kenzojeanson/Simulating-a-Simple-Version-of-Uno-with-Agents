import random
import copy
from Agents import *

class deck:
    def __init__(self, cards, deck_schema, top_card):
        self.cards = cards
        self.deck_schema = deck_schema
        self.top_card = top_card
        
    def reset(self):
        deck = []
        deck = copy.deepcopy(self.deck_schema)
        random.shuffle(deck)
        self.cards = deck
        
Deck = deck(
    cards = [],
    
    deck_schema = [
        'RED 1',
        'RED 2',
        'RED 3',
        'RED 4',
        'RED 5',
        'RED 6',
        'RED 7',
        'RED 8',
        'RED 9',
        'YELLOW 1',
        'YELLOW 2',
        'YELLOW 3',
        'YELLOW 4',
        'YELLOW 5',
        'YELLOW 6',
        'YELLOW 7',
        'YELLOW 8',
        'YELLOW 9',
        'BLUE 1',
        'BLUE 2',
        'BLUE 3',
        'BLUE 4',
        'BLUE 5',
        'BLUE 6',
        'BLUE 7',
        'BLUE 8',
        'BLUE 9',
        'GREEN 1',
        'GREEN 2',
        'GREEN 3',
        'GREEN 4',
        'GREEN 5',
        'GREEN 6',
        'GREEN 7',
        'GREEN 8',
        'GREEN 9',
    ],
    
    top_card = '',
)