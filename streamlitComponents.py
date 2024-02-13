import streamlit as st
from Agents import *

# Streamlit needs this to be called by a function


def initialUI():
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
