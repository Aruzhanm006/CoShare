from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

API_TOKEN = '7777839440:AAHQXPSWYi10EN9Br8SDRjLEHBEzTRsE7Wk'
ADMIN_CHAT_ID = 696134593  

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет! Чтобы пройти верификацию:\n\n"
        "1. Переведи 500₸ на Kaspi: 5151 1234 5678 9012\n"
        "2. Отправь сюда чек в формате PDF\n"
        "Мы передадим его админу для проверки!"
    )

async def handle_pdf(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    document = message.document

    if document and document.mime_type == 'application/pdf':
        caption = f"🧾 Чек (PDF) от @{message.from_user.username or message.from_user.first_name}"
        await context.bot.send_document(chat_id=ADMIN_CHAT_ID, document=document.file_id, caption=caption)
        await message.reply_text("✅ Чек получен и передан админу. Ожидай подтверждения.")
    else:
        await message.reply_text("❗ Пожалуйста, отправьте чек в формате PDF-документа.")

app = ApplicationBuilder().token(API_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.Document.PDF, handle_pdf))
app.add_handler(MessageHandler(filters.Document.ALL, handle_pdf))  

if __name__ == '__main__':
    app.run_polling()
