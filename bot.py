from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from config import TELEGRAM_BOT_TOKEN, AUTHORIZED_USERS
from ai_engine import generate_response
from memory import clear_history
from security import is_authorized
from logger import log_event
from health_check import run_health_check
from commands.analyze import analyze_scan


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    if not is_authorized(user_id, AUTHORIZED_USERS):
        await update.message.reply_text(
            "⛔ Unauthorized access detected."
        )
        return

    clear_history(user_id)

    user = update.effective_user

    log_event(
        f"AUTHORIZED | USER_ID: {user.id} | USERNAME: {user.username} | COMMAND: /start"
    )

    await update.message.reply_text(
        "👋 Welcome back!\n\n"
        "I am JayJay AI Security Assistant 🤖🔐\n"
        "Your conversation memory has been reset.\n\n"
        "Ask me anything about cybersecurity."
    )


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    if not is_authorized(user_id, AUTHORIZED_USERS):
        await update.message.reply_text(
            "⛔ Unauthorized access detected."
        )
        return

    user_message = update.message.text

    user = update.effective_user

    log_event(
        f"AUTHORIZED | USER_ID: {user.id} | USERNAME: {user.username} | MESSAGE: {user_message}"
    )

    # Show a temporary message while the AI is working
    thinking = await update.message.reply_text(
        "🤖 Thinking..."
    )

    # If the message looks like an Nmap scan,
    # analyze it locally instead of sending it to the AI.
    if "/tcp" in user_message and "open" in user_message:
        response = analyze_scan(user_message)
    else:
        response = generate_response(
            user_id,
            user_message,
        )

    # Replace the "Thinking..." message with the answer
    await thinking.edit_text(response)


def main():

    # Run startup health checks
    run_health_check()

    app = Application.builder().token(
        TELEGRAM_BOT_TOKEN
    ).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            message_handler,
        )
    )

    print("🤖 JayJay AI Security Assistant is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
