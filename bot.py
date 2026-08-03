from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# BotFather token
TOKEN = "8870339525:AAGdDtbWMggpA4sOPC9Epg133f_d_P9Du0E"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello Asif! 🤖\nBot Render par successfully chal raha hai ✅"
    )

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Commands:\n/start - bot start karo\n/help - help dekho"
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot started successfully...")

    app.run_polling()


if __name__ == "__main__":
    main()
