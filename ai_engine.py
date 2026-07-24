from openai import OpenAI
from ollama import Client

from config import (
    AI_PROVIDER,
    OPENAI_API_KEY,
    OLLAMA_HOST,
    OLLAMA_MODEL,
)

from memory import (
    add_message,
    get_history,
)

# ----------------------------
# OpenAI Client
# ----------------------------
openai_client = None

if OPENAI_API_KEY:
    openai_client = OpenAI(api_key=OPENAI_API_KEY)

# ----------------------------
# Ollama Client
# ----------------------------
ollama_client = Client(host=OLLAMA_HOST)


def ollama_response(user_id, user_message):
    """
    Generate a response using the local Ollama model.
    """

    # Save the user's message
    add_message(user_id, "user", user_message)

    # Get previous conversation
    history = get_history(user_id)

    # Add system prompt
    messages = [
        {
            "role": "system",
            "content": (
    "You are JayJay AI Security Assistant, a professional "
    "cybersecurity assistant and junior SOC analyst.\n\n"

    "Your expertise includes:\n"
    "- Network security\n"
    "- Vulnerability assessment\n"
    "- Threat detection\n"
    "- Incident response\n"
    "- Linux and Windows security\n"
    "- OWASP Top 10\n"
    "- SIEM concepts\n"
    "- Malware awareness\n"
    "- Security best practices\n\n"

    "Response rules:\n"
    "- Explain concepts clearly for beginners.\n"
    "- Use structured answers with bullet points when helpful.\n"
    "- Include examples from real cybersecurity scenarios.\n"
    "- Focus on defensive security and ethical practices.\n"
    "- Do not provide harmful instructions for illegal activities.\n"
    "- Think like a cybersecurity professional."
),
        }
    ]

    messages.extend(history)

    try:
        response = ollama_client.chat(
            model=OLLAMA_MODEL,
            messages=messages,
            options={
                "temperature": 0.2,
                "num_predict": 180,
                "top_k": 20,
                "top_p": 0.8,
            },
        )

        ai_response = response["message"]["content"]

        # Save assistant response
        add_message(user_id, "assistant", ai_response)

        return ai_response

    except Exception as error:
        print(f"Ollama Error: {error}")

        return (
            "⚠️ I am currently unable to process your request. "
            "Please try again later."
        )


def generate_response(user_id, user_message):
    """
    Main AI response function.
    """

    if AI_PROVIDER == "ollama":
        return ollama_response(user_id, user_message)

    return "⚠️ The selected AI provider is not supported."
