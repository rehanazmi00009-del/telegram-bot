from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from openai import OpenAI
import os

# Telegram Bot Token
TOKEN = "8870339525:AAGWARujsUAWCdiOn4uKzItiN45_AmvkmlU"

# OpenAI API
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 AI Help Bot Online ✅\n\n"
        "📚 Padhai ke sawal\n"
        "🌐 English/Hindi translation\n"
        "💻 Coding help\n"
        "➗ Maths basic solution\n"
        "📝 Application / Letter writing\n"
        "🌍 GK / Current Affairs\n"
        "💪 Motivational guidance\n\n"
        "Use karo:\n/ai tumhara sawal"
    )

# /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Example:\n"
        "/ai python kya hai\n"
        "/ai leave application likho\n"
        "/ai hello ko Hindi mein translate karo\n"
        "/ai 25 + 75 kitna hota hai"
    )

# /ai
async def ai(update: Update, context: ContextTypes.DEFAULT_TYPE):
    question = " ".join(context.args)

    if not question:
        await update.message.reply_text(
            "❓ Sawal likho.\nExample:\n/ai India ki rajdhani kya hai"
        )
        return

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Tum ek helpful Hindi AI teacher ho."},
                {"role": "user", "content": question}
            ]
        )

        answer = response.choices[0].message.content
        await update.message.reply_text(answer)

    except Exception as e:
        await update.message.reply_text(f"⚠️ Error: {e}")


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("ai", ai))

    print("🤖 AI Help Bot chal raha hai...")
    app.run_polling()


if __name__ == "__main__":
    main()
