import random
import copy
from Cards import *
from Agents import *
from queue import Empty
import streamlit as st


class SessionState:
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)


# Session Storage
st.set_page_config(
    page_title="Simulating Uno with Agents",
    page_icon="♠"
)

st.write(f''' 
    \n
    Instructions:
    1. Click on the Prepare/Reset Game Button to deal the cards.
    2. Click on the Start Gameplay Button to start. You only need to press it once since the game runs itself.
    ''')

st.write("-----------------------------------")

        

if 'start_gameplay_button' not in st.session_state:
    st.session_state.start_gameplay_button = False

if 'turn' not in st.session_state:
    st.session_state.turn = 1

if 'game_log' not in st.session_state:
    st.session_state.game_log = {}

if 'players_order' not in st.session_state:
    st.session_state.players_order = [Edison, Daniel, Jack, Kenzo]

if 'current_player_index' not in st.session_state:
    st.session_state.current_player_index = -1

if 'edison_stats' not in st.session_state:
    text = "Edison's stats will go here"
    st.session_state.edison_stats = st.empty()
    st.session_state.edison_stats.markdown(f'''
        <div style="padding: 10px; border: 2px solid #3498db; border-radius: 5px; margin-bottom: 15px">{text}</div>
        ''', unsafe_allow_html=True)

if 'daniel_stats' not in st.session_state:
    text = "Daniel's stats will go here"
    st.session_state.daniel_stats = st.empty()
    st.session_state.daniel_stats.markdown(f'''
        <div style="padding: 10px; border: 2px solid #3498db; border-radius: 5px; margin-bottom: 15px">{text}</div>
        ''', unsafe_allow_html=True)

if 'jack_stats' not in st.session_state:
    text = "Jack's stats will go here"
    st.session_state.jack_stats = st.empty()
    st.session_state.jack_stats.markdown(f'''
        <div style="padding: 10px; border: 2px solid #3498db; border-radius: 5px; margin-bottom: 15px">{text}</div>
        ''', unsafe_allow_html=True)

if 'kenzo_stats' not in st.session_state:
    text = "Kenzo's stats will go here"
    st.session_state.kenzo_stats = st.empty()
    st.session_state.kenzo_stats.markdown(f'''
        <div style="padding: 10px; border: 2px solid #3498db; border-radius: 5px; margin-bottom: 15px">{text}</div>
        ''', unsafe_allow_html=True)


if 'winner_found' not in st.session_state:
    st.session_state.winner_found = False


def ui():
    text = "Edison's stats will go here"
    st.session_state.edison_stats.markdown(f'''
        <div style="padding: 10px; border: 2px solid #3498db; border-radius: 5px; margin-bottom: 15px">{text}</div>
        ''', unsafe_allow_html=True)

    text = "Daniel's stats will go here"
    st.session_state.daniel_stats.markdown(f'''
        <div style="padding: 10px; border: 2px solid #3498db; border-radius: 5px; margin-bottom: 15px">{text}</div>
        ''', unsafe_allow_html=True)

    text = "Jack's stats will go here"
    st.session_state.jack_stats.markdown(f'''
        <div style="padding: 10px; border: 2px solid #3498db; border-radius: 5px; margin-bottom: 15px">{text}</div>
        ''', unsafe_allow_html=True)

    text = "Kenzo's stats will go here"
    st.session_state.kenzo_stats.markdown(f'''
        <div style="padding: 10px; border: 2px solid #3498db; border-radius: 5px; margin-bottom: 15px">{text}</div>
        ''', unsafe_allow_html=True)
    



# ---------- Get Starting Cards ---------- #


def getStartingCards(edison, daniel, jack, kenzo, schema):
    edison_hand = []
    daniel_hand = []
    jack_hand = []
    kenzo_hand = []

    deck = None
    deck = copy.deepcopy(schema)
    random.shuffle(deck)

    for i in range(0, 3):
        edison_hand.append(deck[0])
        deck.pop(0)

        daniel_hand.append(deck[0])
        deck.pop(0)

        jack_hand.append(deck[0])
        deck.pop(0)

        kenzo_hand.append(deck[0])
        deck.pop(0)

        edison.hand = edison_hand
        daniel.hand = daniel_hand
        jack.hand = jack_hand
        kenzo.hand = kenzo_hand

    return deck


# ---------- Get Current Player ---------- #
def getNextPlayer(players_order, current_player_index, play_order):
    next_player = players_order[current_player_index]
    if play_order == 'Clockwise':
        current_player_index += 1
        if current_player_index != len(players_order):
            next_player = players_order[current_player_index]

        elif current_player_index == len(players_order):
            current_player_index = 0
            next_player = players_order[0]

    else:
        next_player = players_order[current_player_index - 1]

    return next_player, current_player_index


def getTopCard(deck):
    if deck.top_card == '':
        top_card = deck.cards[0]
        deck.cards.pop(0)

    else:
        top_card = deck.top_card
    return top_card


def checkforWinner(current_player):
    winner = False
    if len(current_player.hand) == 0:
        winner = True
        st.write(current_player.name, 'has won! Congrats!')

    return winner


############################################

with st.sidebar:
    if st.button('Prepare/Reset Game') == True:
        

        st.session_state.winner_found = False
        ui()
        Deck.cards = getStartingCards(
            Edison, Daniel, Jack, Kenzo, Deck.deck_schema)
        Deck.top_card = ''
        Deck.top_card = getTopCard(Deck)

        st.session_state.edison_stats.markdown(f'''
        <div style="padding: 10px; border: 2px solid #3498db; border-radius: 5px; margin-bottom: 15px"> <strong>Edison's Hand </strong><br>{Edison.hand}</div>
        ''', unsafe_allow_html=True)

        st.session_state.daniel_stats.markdown(f'''
        <div style="padding: 10px; border: 2px solid #3498db; border-radius: 5px; margin-bottom: 15px"><strong>Daniel's Hand </strong><br>{Daniel.hand}</div>
            ''', unsafe_allow_html=True)

        st.session_state.jack_stats.markdown(f'''
        <div style="padding: 10px; border: 2px solid #3498db; border-radius: 5px; margin-bottom: 15px"><strong>Jack's Hand </strong><br>{Jack.hand}</div>
            ''', unsafe_allow_html=True)

        st.session_state.kenzo_stats.markdown(f'''
        <div style="padding: 10px; border: 2px solid #3498db; border-radius: 5px; margin-bottom: 15px"><strong>Kenzo's Hand </strong><br>{Kenzo.hand}</div>
            ''', unsafe_allow_html=True)

        st.write('Cards left in deck:', len(Deck.cards))
        st.write('Current Top Card:', Deck.top_card)

    st.session_state.start_gameplay_button = st.button("Start Gameplay")

    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

    import time
    if st.session_state.start_gameplay_button == True:

        while st.session_state.winner_found == False:
            time.sleep(2)
            current_player, st.session_state.current_player_index = getNextPlayer(
                st.session_state.players_order, st.session_state.current_player_index, "Clockwise")

            initial_top_card = Deck.top_card

            print(Deck.cards, '\n')

            # Player Action
            print('CURRENTPLAYER:', current_player)
            card_pickup, card_putdown, action_log = performActionAgent(
                current_player, Deck.top_card, current_player.hand)

            # Picks up a card
            if card_pickup == "TRUE":
                card_pickup = Deck.cards[0]
                Deck.cards.pop(0)
                current_player.hand.append(card_pickup)

                if len(Deck.cards) == 0:
                    Deck.reset()

            # Puts down a card
            if card_putdown != "FALSE":
                current_player.hand.remove(card_putdown)
                Deck.top_card = card_putdown

            # Update text
            st.session_state.edison_stats.markdown(f'''
            <div style="padding: 10px; border: 2px solid #3498db; border-radius: 5px; margin-bottom: 15px"> <strong>Edison's Hand </strong><br>{Edison.hand}</div>
            ''', unsafe_allow_html=True)

            st.session_state.daniel_stats.markdown(f'''
            <div style="padding: 10px; border: 2px solid #3498db; border-radius: 5px; margin-bottom: 15px"><strong>Daniel's Hand </strong><br>{Daniel.hand}</div>
                ''', unsafe_allow_html=True)

            st.session_state.jack_stats.markdown(f'''
            <div style="padding: 10px; border: 2px solid #3498db; border-radius: 5px; margin-bottom: 15px"><strong>Jack's Hand </strong><br>{Jack.hand}</div>
                ''', unsafe_allow_html=True)

            st.session_state.kenzo_stats.markdown(f'''
            <div style="padding: 10px; border: 2px solid #3498db; border-radius: 5px; margin-bottom: 15px"><strong>Kenzo's Hand </strong><br>{Kenzo.hand}</div>
                ''', unsafe_allow_html=True)

            st.session_state.game_log[f'Turn {st.session_state.turn}'] = {
                'Turn': st.session_state.turn,
                'Player': current_player.name,
                'Initial Top Card': initial_top_card,
                'Card Pickup': card_pickup,
                'Card Putdown': card_putdown,
                'Cards Left in Deck': len(Deck.cards),
                'Current Top Card': Deck.top_card
            }

            st.write(f'Turn {st.session_state.turn}',
                     st.session_state.game_log[f'Turn {st.session_state.turn}'])

            st.session_state.turn += 1

            st.session_state.winner_found = checkforWinner(current_player)
            


