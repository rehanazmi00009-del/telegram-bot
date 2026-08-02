from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Aapka Telegram Bot Token
TOKEN = "8870339525:AAGdDtbWMggpA4sOPC9Epg133f_d_P9Du0E"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello Rehan! Bot chal raha hai ✅")

# Bot setup
app = ApplicationBuilder().token(TOKEN).build()

# Command handler add karo
app.add_handler(CommandHandler("start", start))

print("Bot chal raha hai...")

# Bot start karo
app.run_polling()
