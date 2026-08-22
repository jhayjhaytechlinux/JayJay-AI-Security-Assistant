from collections import defaultdict

MAX_HISTORY = 2

conversation_memory = defaultdict(list)


def add_message(user_id, role, content):
    """
    Store a message for a user.
    """

    conversation_memory[user_id].append(
        {
            "role": role,
            "content": content,
        }
    )

    conversation_memory[user_id] = conversation_memory[user_id][-MAX_HISTORY:]


def get_history(user_id):
    """
    Return conversation history.
    """

    return conversation_memory[user_id]


def clear_history(user_id):
    """
    Clear a user's conversation history.
    """

    conversation_memory[user_id] = []
