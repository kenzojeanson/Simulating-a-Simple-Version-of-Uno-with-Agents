import streamlit as st
import time
from Cards import *
from Agents import *
from streamlitComponents import *
from functions import *

# Setting up the UI and its background values
initialUI()

# Prepare the game
with st.sidebar:
    if st.button('Prepare/Reset Game') == True:
        st.session_state.winner_found = False

        ui()

        Deck.cards = getStartingCards(
            Edison, Daniel, Jack, Kenzo, Deck.deck_schema)
        Deck.top_card = getTopCard(Deck)

        updateHand(Deck, Edison, Daniel, Jack, Kenzo)

    # Gameplay Loop
    st.session_state.start_gameplay_button = st.button("Start Gameplay")
    if st.session_state.start_gameplay_button == True:
        while st.session_state.winner_found == False:
            time.sleep(1)
            current_player, st.session_state.current_player_index = getNextPlayer(
                st.session_state.players_order, st.session_state.current_player_index, "Clockwise")

            initial_top_card = Deck.top_card

            # Player Action (Agent picks the best move)
            print('CURRENTPLAYER:', current_player)
            card_pickup, card_putdown, action_log = performActionAgent(
                current_player, Deck.top_card)

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

            # Update text and values
            updateValues(current_player, initial_top_card, card_pickup,
                         card_putdown, Deck, Edison, Daniel, Jack, Kenzo)
