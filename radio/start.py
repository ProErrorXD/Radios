from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup 
from config import BOT_USERNAME, BOT_NAME

@Client.on_message(filters.command("start"))
async def start(client, m: Message):
   if m.chat.type == 'private':
       await m.reply(f"**Hey I am Radio Bot 📻\n\n** \n`Add this @{BOT_USERNAME} to your Group and Make it Admin \n2) Add`  `to your Group` \n3) **Commands** : \n`/radio` Ytlink Live \n`/stop`",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                     InlineKeyboardButton(
                                            "Support", url="t.me/DeCodeSupport")
                                    ]]
                            ))
   else:
      await m.reply(f"**@{BOT_NAME} is Alive! ✨**")
