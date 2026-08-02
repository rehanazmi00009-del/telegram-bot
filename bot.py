from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Apna Telegram Bot Token yahan likho
TOKEN = "8870339525:AAGdDtbWMggpA4sOPC9Epg133f_d_P9Du0E"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hello Rehan!\\n\\n🤖 Bot bilkul sahi chal raha hai ✅"
    )

# Normal message ka reply
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"📩 Aapne bheja: {text}")

# Bot build karo
app = ApplicationBuilder().token(TOKEN).build()

# Handlers add karo
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

print("✅ Telegram Bot chal raha hai...")

# Bot start karo
app.run_polling()
