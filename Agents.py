import autogen
from env import API_KEY
api_key = API_KEY

config_list = [
    {
        'model': 'gpt-4-1106-preview',
        'api_key': api_key,
    }
]
# User Proxy
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    llm_config={
        "cache_seed": 42,  # seed for caching and reproducibility
        "config_list": config_list,  # a list of OpenAI API configurations
        "temperature": 0,  # temperature for sampling
    },
    max_consecutive_auto_reply=1,
    is_termination_msg=lambda x: x.get(
        "content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        "work_dir": "coding",
        "use_docker": False,
    },
    system_message=f"""
    You are a UNO player who is using an assistant to get advice on the next best move. 
    You have simple instructions:
    Instruction 1 - You will first send out the initial chat message to the Assistnat
    Instruction 2 - After that, you should expect a response structured like this:
    [START]
    "player": "Player Name",
    "card_pickup": "TRUE",
    "card_putdown": "BLUE 3"
    [END]
     
    If you receive this, then reply "TASK COMPLETED TO FULL SATISFACTION. TERMINATE DISCUSSION" and terminate the conversation to not waste any more time. 
    Else, tell the assistant that you need their response in that format. 
    """)

# Player
player_agent = autogen.ConversableAgent(
    name="assistant",
    llm_config={
        "cache_seed": 42,  # seed for caching and reproducibility
        "config_list": config_list,  # a list of OpenAI API configurations
        "temperature": 0,  # temperature for sampling
    },  # configuration for autogen's enhanced inference API which is compatible with OpenAI API
)


def performActionAgent(current_player, top_card, agent_hand):
    user_proxy.initiate_chat(
        current_player.agent,
        message=f'''
        [Persona]: Your name is {current_player.name}. You are a helpful assistant who does not make errors. Your job is to give advice on the best next move in UNO. \n
        You will be given instructions below. Talk through and think out loud for each instruction. 
        [Your Instructions]:
            Step 1 - Ensure that you know the rules of UNO. However, also note that this version has no Plus2, Plus4, or Wildcards. Also, you cannot put down a card after picking it up. Hence, picking up a card ends your turn. 
            Step 2 - Observe the cards in Your Hand. This will be delineated by "Your Hand". 
            Step 3 - Cards are in the format of "COLOUR NUMBER". Repeat the COLOUR NUMBER combination for each of your cards.
            Step 4 - Observe the Top Card. This will be delineated by "Top Card".
            Step 5 - Decide on what the best move is. This could be either putting down a card, or picking up a card from the deck. Look at whether the Top Card matches COLOUR or NUMBER as per any of your cards. 
            Step 6 - Once you have decided on the next best move, map out your move using the mapping below:
            
                "player": Your name
                "card_pickup": If you pick up a card, this should be "TRUE". If you did not pick up a card from the deck, this should be "FALSE"
                "card_putdown": The card you put down. If you did not put down a card, this should be "FALSE"
                    
            Step 7 - Once you have decided on the next best move, recreate the template below. This is not code. \n
        
        Here is an example output which you should replicate:
        [START]
        "player": "Player Name",
        "card_pickup": "TRUE",
        "card_putdown": "BLUE 3"
        [END]
        \n
    
    [Information]:
    Top Card: {top_card} \n
    Your Hand: {agent_hand} \n
    
    [Special Instruction]:
    If you receive "TASK COMPLETED TO FULL SATISFACTION", then terminate the conversation and do not waste any more time.
    Let's think step by step.
    ''',
    )

    #print(player_agent.chat_messages)

    key = list(player_agent.chat_messages.keys())[0]
    chatlog = player_agent.chat_messages[key]

    full_text = ''
    for chat in chatlog:
        full_text += chat['content'] + ' '
    import re

    pattern = r'\[START\](.*?)\[END\]'

    matches = re.findall(pattern, full_text, re.DOTALL)
    action = matches[-1].strip()
    action = "{" + action + "}"
    action = re.sub('\n', '', action)

    import ast
    action = ast.literal_eval(action)

    #print(action)
    card_pickup = action['card_pickup']
    card_putdown = action['card_putdown']
    
    return card_pickup, card_putdown, action

######################################


class player:
    def __init__(self, name, hand, agent):
        self.name = name
        self.hand = hand
        self.agent = agent


Edison = player(
    name="Edison",

    hand=[],

    agent=player_agent
)

Daniel = player(
    name="Daniel",

    hand=[],

    agent=player_agent
)

Jack = player(
    name="Jack",

    hand=[],

    agent=player_agent
)


Kenzo = player(
    name="Kenzo",

    hand=[],

    agent=player_agent
)
