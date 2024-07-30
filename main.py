import io
import logging

from telegram import Update
from telegram.ext import (ApplicationBuilder, CommandHandler, ContextTypes,
                          MessageHandler, filters)

from speech_to_text import speech_to_text_whisper
import os
from settings import settings

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    This function is called when the user sends the /start command to the bot.

    Parameters
    ----------
    update : Update
        object that contains all the information and data that are coming from Telegram
        itself (like the message, the user who issued the command, etc)
    context : ContextTypes.DEFAULT_TYPE
        object that contains information and data about the status of the library
        itself (like the Bot, the Application, the job_queue, etc).
    """
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!"
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    This function is called when the user sends a message to the bot. It echoes the message back to the user.

    Parameters
    ----------
    update : Update
        Object that contains all the information and data that are coming from Telegram
        itself (like the message, the user who issued the command, etc).
    context : ContextTypes.DEFAULT_TYPE
        Object that contains information and data about the status of the library
        itself (like the Bot, the Application, the job_queue, etc).
    """
    if update.message and update.message.text:
        await context.bot.send_message(
            chat_id=update.effective_chat.id, text=update.message.text
        )
    else:
        logging.info("Received a message without text, ignoring.")


async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    This function is called when the user sends the /caps command to the bot.
    It converts the text to uppercase.
    """
    text_caps = " ".join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


async def translate_voice(update, context):
    print("translate_voice")

    file = await context.bot.get_file(update.message.voice.file_id)
    file_path = os.path.join("downloads", f"{file.file_id}.oga")
    await file.download_to_drive(file_path)

    text = speech_to_text_whisper(file_path)
    logging.info(f"Text: {text}")
    if not text:
        text = "I don't understand this file"

    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)


if __name__ == "__main__":
    application = ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN).build()

    start_handler = CommandHandler("start", start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    caps_handler = CommandHandler("caps", caps)
    voice_handler = MessageHandler(filters.VOICE, translate_voice)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(caps_handler)
    application.add_handler(voice_handler)

    application.run_polling()
