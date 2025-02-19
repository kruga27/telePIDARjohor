from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import csv
import re

TOKEN = "YOUR_BOT_API_TOKEN"

async def handle_message(update: Update, context):
    text = update.message.text

    # Example: Extract values from text
    match = re.match(r"RE:\s*(\d+)/(\d+)=([\d.]+)", text)
    if match:
        re_60, re_30, re_index = match.groups()
        
        # Store in CSV
        with open("data.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([re_60, re_30, re_index])

        await update.message.reply_text(f"Data saved: {re_60}, {re_30}, {re_index}")

app = Application.builder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
