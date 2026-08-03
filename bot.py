from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# 🔑 Apna NAYA Bot Token yahan dalo
TOKEN = "8870339525:AAG6-t_qAVxIP3i-h1ZJeSBXOo0cgK3uzdk"

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello Rehan! 🤖\nBot Render par successfully chal raha hai ✅"
    )

# /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Available Commands:\n/start - Bot start karo\n/help - Help dekho\n/about - Bot ke baare mein\n/photo - Photo pao"
    )

# /about
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Yeh Rehan ka Telegram Bot hai.\n🚀 Render par 24x7 chal raha hai."
    )

# /photo
async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo="https://picsum.photos/400/300",
        caption="📷 Hello Rehan! Yeh tumhare bot ki test photo hai ✅"
    )

# App banaye
app = Application.builder().token(TOKEN).build()

# Handlers add kare
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("about", about))
app.add_handler(CommandHandler("photo", photo))

print("🤖 Rehan Bot started successfully...")

# Bot chalu kare
app.run_polling()
