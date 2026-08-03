import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8870339525:AAGWARujsUAWCdiOn4uKzItiN45_AmvkmlU"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello Rehan! Bot chal raha hai ✅")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Commands:\\n/start - Bot start kare\\n/help - Madad dekhe"
    )

async def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot chal raha hai...")

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    # Bot ko chalu rakho
    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
