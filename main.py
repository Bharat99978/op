from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import time

# Replace with your API key
API_KEY = '7228147192:AAEg1GtZGTGSr_uag1BMi2V6hwytNBBYb8o'

# Variables to track time
start_time = None
elapsed_time = 0
running = False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Welcome to the Stopwatch bot! Use /startwatch to start the stopwatch.")

async def startwatch(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global start_time, running
    if running:
        await update.message.reply_text("Stopwatch is already running.")
    else:
        start_time = time.time() - elapsed_time  # resume from last elapsed time
        running = True
        await update.message.reply_text("Stopwatch started!")

async def stopwatch(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global elapsed_time
    if running:
        elapsed_time = time.time() - start_time
        await update.message.reply_text(f"Elapsed time: {elapsed_time:.2f} seconds.")
    else:
        await update.message.reply_text("Stopwatch is not running. Use /startwatch to start.")

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global running, elapsed_time
    if running:
        elapsed_time = time.time() - start_time
        running = False
        await update.message.reply_text(f"Stopwatch stopped at {elapsed_time:.2f} seconds.")
    else:
        await update.message.reply_text("Stopwatch is not running.")

async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global start_time, elapsed_time, running
    start_time = None
    elapsed_time = 0
    running = False
    await update.message.reply_text("Stopwatch has been reset.")

def main() -> None:
    app = Application.builder().token(API_KEY).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("startwatch", startwatch))
    app.add_handler(CommandHandler("stopwatch", stopwatch))
    app.add_handler(CommandHandler("stop", stop))
    app.add_handler(CommandHandler("reset", reset))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()