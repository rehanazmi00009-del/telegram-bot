from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# 👇 अपना Bot Token यहाँ डालो
TOKEN = "8870339525:AAG6-t_qAVxIP3i-h1ZJeSBXOo0cgK3uzdk"

# /start कमांड
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello Rehan! Bot chal raha hai ✅")

# /help कमांड
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Commands:\\n/start - Bot start kare\\n/help - Madad dekhe")

# मुख्य फ़ंक्शन
def main():
    app = Application.builder().token(TOKEN).build()

    # Commands जोड़ना
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot chal raha hai...")

    # Bot शुरू करना
    app.run_polling()


if __name__ == "__main__":
  main()
    
