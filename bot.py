from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = 8870339525:AAH5lVVToVR3XgW4i52WNafExWOud4BJt9Q

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello Asif! Bot chal raha hai.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot chal raha hai...")
app.run_polling()8870339525:AAH5lVVToVR3XgW4i52WNafExWOud4BJt9Q