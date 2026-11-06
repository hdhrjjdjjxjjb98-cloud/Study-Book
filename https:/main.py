from telegram.ext import Application, CommandHandler, MessageHandler, filters
import os
from telegram import Update
async def start(update: Update, context):
    await update.message.reply_text(
        "أهلاً بيك في بوت الاختبارات 📚\nاختار المادة اللي عايز تختبر نفسك فيها."
    )
  async def help_command(update: Update, context):
    await update.message.reply_text(
        "البوت ده مخصص لاختبارات المنهج الدراسي 📖"
    )

async def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("البوت يعمل الآن...")
    await app.initialize()
    await app.start()
    await app.updater.start_polling()

import asyncio

if name == "main":
    asyncio.run(main())
