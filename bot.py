import asyncio
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


async def main():
    app = Application.builder().token(TOKEN).build()

    # handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot started successfully...")

    # start bot
    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    # bot ko hamesha chalu rakho
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
