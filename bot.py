from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from config import (
    TELEGRAM_BOT_TOKEN,
    AUTHORIZED_USERS,
    AI_PROVIDER,
    OLLAMA_MODEL,
)

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


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    if not is_authorized(user_id, AUTHORIZED_USERS):
        await update.message.reply_text(
            "⛔ Unauthorized access detected."
        )
        return

    await update.message.reply_text(
        "🛡️ JayJay AI Security Assistant Commands\n\n"
        "/start - Start the assistant\n"
        "/help - Show available commands\n"
        "/about - About this project\n"
        "/status - Show system status\n"
        "/clear - Clear conversation memory\n\n"
        "Capabilities:\n"
        "🤖 AI cybersecurity assistant\n"
        "🔎 Vulnerability explanations\n"
        "📄 Nmap XML analysis\n"
        "📑 PDF security reports\n"
        "🛡️ Defensive security guidance"
    )


async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    if not is_authorized(user_id, AUTHORIZED_USERS):
        await update.message.reply_text(
            "⛔ Unauthorized access detected."
        )
        return

    await update.message.reply_text(
        "🛡️ JayJay AI Security Assistant\n\n"
        "An AI-powered cybersecurity assistant designed "
        "for security learning, vulnerability analysis, "
        "and defensive security operations.\n\n"

        "Technology Stack:\n"
        "🐍 Python\n"
        "🤖 Ollama Local AI\n"
        "🧠 Phi-3 Mini LLM\n"
        "📱 Telegram Bot API\n"
        "🐧 Ubuntu WSL\n\n"

        "Security Capabilities:\n"
        "✅ Vulnerability explanations\n"
        "✅ OWASP security guidance\n"
        "✅ Nmap XML analysis\n"
        "✅ Automated PDF reports\n"
        "✅ Local AI processing\n\n"

        "Security Mode:\n"
        "🔐 Defensive Security Only\n\n"

        "Built by JayJay 🚀"
    )


async def status_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    if not is_authorized(user_id, AUTHORIZED_USERS):
        await update.message.reply_text(
            "⛔ Unauthorized access detected."
        )
        return

    await update.message.reply_text(
        "🟢 JayJay AI Security Assistant Status\n\n"
        "AI Provider:\n"
        f"✅ {AI_PROVIDER}\n\n"
        "Model:\n"
        f"✅ {OLLAMA_MODEL}\n\n"
        "Memory:\n"
        "✅ Active\n\n"
        "Security Mode:\n"
        "✅ Defensive Only"
    )


async def clear_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    if not is_authorized(user_id, AUTHORIZED_USERS):
        await update.message.reply_text(
            "⛔ Unauthorized access detected."
        )
        return

    clear_history(user_id)

    await update.message.reply_text(
        "🧹 Conversation memory cleared successfully."
    )


def main():

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


    app.add_handler(
        CommandHandler(
            "help",
            help_command,
        )
    )


    app.add_handler(
        CommandHandler(
            "about",
            about_command,
        )
    )


    app.add_handler(
        CommandHandler(
            "status",
            status_command,
        )
    )


    app.add_handler(
        CommandHandler(
            "clear",
            clear_command,
        )
    )


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
