import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram import Update
import time
import os
import asyncio

logging.basicConfig(level=logging.INFO)

# It's highly recommended to get the token from an environment variable for security
# For example, before running your script:
# export TELEGRAM_BOT_TOKEN='token'
#TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'YOUR_DEFAULT_TOKEN_IF_NOT_SET') 
TOKEN = 'xcvcxvcxvxcvxcvxcvxvxc'
# Define your async functions
async def start(update: Update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Olá! Sou um bot de teste.')

async def processa_pergunta(update: Update, context):
    pergunta = update.message.text
    # TO DO
    #colocar tempo
    # Processar a resposta, condicionais (ver a lista de opções; IF 1 ; faça isso
    #
    resposta = 'Essa é a resposta para a pergunta: ' + pergunta
    await update.message.reply_text(resposta) # Using reply_text is often better for direct replies
    # Note: time.sleep() will block the event loop in an async function.
    # If you need a delay, use asyncio.sleep(). However, for a simple reply,
    # a delay might not be necessary or desirable here.
    # If you *must* have a delay before the response is sent, use:
    # import asyncio
    # await asyncio.sleep(2) 

def main():
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()

    # Get the dispatcher from the application
    # dp = application.dispatcher # This line is no longer necessary as handlers are added directly to the application

    # Add handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, processa_pergunta))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(poll_interval=3) # poll_interval is optional, defaults to 0.0
    # application.run_polling() is asynchronous and handles polling for you.
    # .idle() is not typically used with Application.run_polling()
    # It's more for when you manually manage the event loop.

if __name__ == '__main__':
    # Set your token as an environment variable before running the script
    # Example for testing:
    # os.environ['TELEGRAM_BOT_TOKEN'] = '7449014851:AAGOgjDhSRISbKwyT54EherGK8DXsmMntoQ'
    main()
