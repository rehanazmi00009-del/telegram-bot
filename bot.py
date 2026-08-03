from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# अपना Bot Token
TOKEN = "8870339525:AAGWARujsUAWCdiOn4uKzItiN45_AmvkmlU"


# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello Rehan! Bot chal raha hai ✅"
    )


# /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Commands:\\n"
        "/start - Bot start kare\\n"
        "/help - Madad dekhe\\n"
        "/owner - Owner ki jankari\\n"
        "/teacher - Teacher ki jankari"
    )


# /owner
async def owner(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👑 Owner: Rehan Azmi\\n"
        "📱 Telegram: @cpvipx666"
    )


# /teacher
async def teacher(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👨‍🏫 Teacher: Rehan Sir\\n"
        "📚 Python & Telegram Bot Support"
    )


def main():
    app = Application.builder().token(TOKEN).build()

    # Commands add karo
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("owner", owner))
    app.add_handler(CommandHandler("teacher", teacher))

    print("Bot chal raha hai...")

    app.run_polling()


if __name__ ==__ "main__":
    main()
