from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from config import TELEGRAM_BOT_TOKEN, AUTHORIZED_USERS
from memory import clear_history
from security import is_authorized
from logger import log_event
from health_check import run_health_check

from handlers import (
    message_handler,
    xml_handler,
)


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


def main():

    # Run startup health checks
    run_health_check()

    app = (
        Application.builder()
        .token(TELEGRAM_BOT_TOKEN)
        .build()
    )

    app.add_handler(
        CommandHandler(
            "start",
            start,
        )
    )

    # Handle uploaded XML files
    app.add_handler(
        MessageHandler(
            filters.Document.FileExtension("xml"),
            lambda update, context: xml_handler(
                update,
                context,
                AUTHORIZED_USERS,
                is_authorized,
            ),
        )
    )

    # Handle normal text messages
    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            lambda update, context: message_handler(
                update,
                context,
                AUTHORIZED_USERS,
                is_authorized,
            ),
        )
    )

    print("🤖 JayJay AI Security Assistant is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
