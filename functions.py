import streamlit as st
import copy
import random

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


def updateValues(current_player, initial_top_card, card_pickup, card_putdown, Deck, Edison, Daniel, Jack, Kenzo):
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
    
    
def updateHand(Deck, Edison, Daniel, Jack, Kenzo):
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