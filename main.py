from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery



KingAbhi = Client(
      name="PyrogramBot",
      bot_token="5805245861:AAEkDOk9qLRts5px8vF1vm2bslC3cH5KFZg",
      api_id="26974083",
      api_hash="e013696bd13ea9495b803a679852da59"
)



START_MESSAGE = """
HELLO {} I AM PYROGRAM BOT UNDER CONSTRUCTION
"""



HELP_MESSAGE = """
DONT SHIT HERE
"""





START_BUTTON = [[
    InlineKeyboardButton("Dev🤴🏿", url="t.me/clause07")
    ],[
    InlineKeyboardButton("😯HELP", callback_data="help"),
    InlineKeyboardButton("INFO👀", callback_data="info")
    ],[
    InlineKeyboardButton("🏴‍☠️Delete", callback_data="delete")
    ]]
 




@KingAbhi.on_message(filters.command("start"))
async def start_message(bot, message):
         await message.reply_text(
                  text=START_MESSAGE.format(message.from_user.mention),
                  reply_markup=InlineKeyboardMarkup(START_BUTTON)
         )
                 
    

                 



@KingAbhi.on_message(filters.command("help"))
async def help_message(bot : KingAbhi, message: Message):
         await message.reply_text(
                  text="HELP_MESSAGE"
         )



@KingAbhi.on_message(filters.command("info"))
async def info(bot, msg):
         text = f"""
👉🏿Name - {msg.from_user.first_name}
👉🏿UserName - @{msg.from_user.username}
👉🏿Id - {msg.from_user.id}
👉🏿Mention - {msg.from_user.mention}"""

         await msg.reply_text(text=text)
      

@KingAbhi.on_callback_query()
async def callback(client: KingAbhi, update: CallbackQuery):

        if update.data == "help":
             await update.message.edit(
                     text=f"""
HELLO {message.from_user.mention} I AM PYROGRAM BOT UNDER CONSTRUCTION
""",
                     reply_markup=InlineKeyboardMarkup(START_BUTTON)
             )


        elif update.data == "info":
             await update.message.edit(
                     text= f"""
👉🏿Name - {msg.from_user.first_name}
👉🏿UserName - @{msg.from_user.username}
👉🏿Id - {msg.from_user.id}
👉🏿Mention - {msg.from_user.mention}""",
                     reply_markup=InlineKeyboardMarkup(START_BUTTON)
             )

        elif update.data == "delete":
             await update.message.delete()

print("Bot Started")

KingAbhi.run()
