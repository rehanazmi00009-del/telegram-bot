from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# अपना Telegram Bot Token यहाँ डालो
TOKEN = "8870339525:AAGdDtbWMggpA4sOPC9Epg133f_d_P9Du0E"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello Asif! 🤖\nBot Render par successfully chal raha hai ✅"
    )

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Available commands:\n/start - Bot start karo\n/help - Help dekho"
    )

def main():
    app = Application.builder().token(TOKEN).build()

    # Handlers add karo
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot started successfully...")

    # Bot start karo
    app.run_polling()


if name == "main":
    main()
