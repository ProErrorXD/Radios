from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from radio.radio import app

bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="radio"),
)

bot.start()
app.start()
idle()
