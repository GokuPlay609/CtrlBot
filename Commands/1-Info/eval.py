import json
from telegram.ext import Application, CommandHandler, ContextTypes
from settings import BOT_TOKEN  # Import the bot token from settings.py

# Load VIP users from JSON file
def load_vips(chat_id):
    with open(f"Accounts/{chat}/vips.json", "r") as f:
        return json.load(f)

# Check if user is VIP
def is_vip(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    vips = load_vips(chat_id)
    return user_id in vips

# Define a command handler that checks if user is VIP before running the code
async def vip_only_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_vip(update, context):
        await update.message.reply_text("You are not authorized to use this command.")
        return
    # Get the custom Python command from the message text
    command = update.message.text.split(" ", 1)[1]
    try:
        # Run the custom Python command using eval
        result = eval(command)
        await update.message.reply_text(f"Result: {result}")
    except Exception as e:
        await update.message.reply_text(f"Error: {e}")

# Create a Telegram application
application = Application.builder().token(BOT_TOKEN).build()

# Add the VIP-only command handler
application.add_handler(CommandHandler("run", vip_only_handler))

# Run the bot
application.run_polling()
