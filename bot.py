from telegram.ext import Application, CommandHandler

TOKEN = "8870339525:AAGdDtbWMggpA4sOPC9Epg133f_d_P9Du0E"

async def start(update, context):
    await update.message.reply_text("Hello Asif! Bot chal raha hai ✅")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

if name == "main":
    print("Bot started...")
    app.run_polling()
