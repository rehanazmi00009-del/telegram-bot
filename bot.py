from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8870339525:AAGdDtbWMggpA4sOPC9Epg133f_d_P9Du0E"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hello Rehan! Bot bilkul sahi chal raha hai."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Bot start karo\n/help - Madad dekho"
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot chal raha hai...")
    app.run_polling(close_loop=False)

# नीचे की लाइन बिल्कुल ऐसी ही होनी चाहिए
if name == "main":
    main()
