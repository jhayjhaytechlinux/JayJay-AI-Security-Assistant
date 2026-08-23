"""
Telegram message and document handlers.
"""

import os

from ai_engine import generate_response
from commands.analyze import analyze_scan
from commands.analyze_xml import analyze_xml
from logger import log_event
from reports.pdf_report import generate_pdf_report


async def send_safe_message(message, text):
    """
    Send Telegram messages safely.
    Handles long AI responses.
    """

    max_length = 4000

    if len(text) <= max_length:
        await message.edit_text(text)
        return

    parts = [
        text[i:i + max_length]
        for i in range(0, len(text), max_length)
    ]

    await message.edit_text(parts[0])

    for part in parts[1:]:
        await message.reply_text(part)


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

        pdf_file = generate_pdf_report(
            target="Manual Scan",
            report_text=response,
        )

        await send_safe_message(
            thinking,
            response,
        )

        with open(pdf_file, "rb") as pdf:
            await update.message.reply_document(
                document=pdf,
                filename=os.path.basename(pdf_file),
                caption=(
                    "🛡️ JayJay AI Security Assessment Report\n\n"
                    "✅ PDF report generated successfully."
                ),
            )

        return

    response = generate_response(
        user_id,
        user_message,
    )

    await send_safe_message(
        thinking,
        response,
    )


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

    pdf_file = generate_pdf_report(
        target=document.file_name,
        report_text=response,
    )

    await send_safe_message(
        thinking,
        response,
    )

    with open(pdf_file, "rb") as pdf:
        await update.message.reply_document(
            document=pdf,
            filename=os.path.basename(pdf_file),
            caption=(
                "🛡️ JayJay AI Security Assessment Report\n\n"
                "✅ PDF report generated successfully."
            ),
        )
