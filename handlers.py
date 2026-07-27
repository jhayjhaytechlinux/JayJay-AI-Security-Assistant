"""
Telegram message and document handlers.
"""

import os

from commands.analyze import analyze_scan
from commands.analyze_xml import analyze_xml
from ai_engine import generate_response
from logger import log_event


async def message_handler(update, context, authorized_users, is_authorized):
    """
    Handle normal text messages.
    """

    user_id = update.effective_user.id

    if not is_authorized(user_id, authorized_users):
        await update.message.reply_text(
            "⛔ Unauthorized access detected."
        )
        return

    user_message = update.message.text

    log_event(
        f"AUTHORIZED | USER_ID: {user_id} | MESSAGE: {user_message}"
    )

    thinking = await update.message.reply_text(
        "🤖 Thinking..."
    )

    if "/tcp" in user_message and "open" in user_message:
        response = analyze_scan(user_message)
    else:
        response = generate_response(
            user_id,
            user_message,
        )

    await thinking.edit_text(response)


async def xml_handler(update, context, authorized_users, is_authorized):
    """
    Handle uploaded Nmap XML files.
    """

    user_id = update.effective_user.id

    if not is_authorized(user_id, authorized_users):
        await update.message.reply_text(
            "⛔ Unauthorized access detected."
        )
        return

    document = update.message.document

    if not document.file_name.lower().endswith(".xml"):
        await update.message.reply_text(
            "❌ Please upload a valid Nmap XML file."
        )
        return

    thinking = await update.message.reply_text(
        "📄 Downloading XML scan..."
    )

    telegram_file = await context.bot.get_file(document.file_id)

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join(
        "uploads",
        document.file_name,
    )

    await telegram_file.download_to_drive(file_path)

    response = analyze_xml(file_path)

    await thinking.edit_text(response)
