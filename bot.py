from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# अपना Telegram Bot Token यहाँ डालो
TOKEN = "8870339525:AAGdDtbWMggpA4sOPC9Epg133f_d_P9Du0E"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hello Rehan!\\n🤖 Bot bilkul sahi chal raha hai."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Bot start karo\\n/help - Madad dekho"
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("✅ Bot chal raha hai...")

    # Python 3.14 error se bachne ke liye
    app.run_polling(close_loop=False)


if __name__ == "__main__":
    main()
