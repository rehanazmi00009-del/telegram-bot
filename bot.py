from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Telegram Bot Token
TOKEN = "8870339525:AAGdDtbWMggpA4sOPC9Epg133f_d_P9Du0E"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello Rehan! Bot chal raha hai ✅")

# Create bot app
app = ApplicationBuilder().token(TOKEN).build()

# Add command handler
app.add_handler(CommandHandler("start", start))

# Start bot
print("Bot chal raha hai...")
app.run_polling()
