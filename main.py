from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery
import random   


TakeMehDown=Client(
         "Pyrogram Bot",
         bot_token="5533296789:AAE1Rpz3ppw9b-XGWPqY3GekKIENreN1ACs",
         api_id="1641138",
         api_hash="49db06aedd730fd89dd0fc9c84fd656f"
)


ALL_PICS = [ 
 "https://telegra.ph/file/702d8555404645e94e6fb.jpg",
 "https://telegra.ph/file/ecf7954d4e47d10c5becb.jpg",
 "https://telegra.ph/file/71bed9d4da74ec5c341a1.jpg"
]


START_MESSAGE = """
Hey {} Wassup!!🤖
"""


@TakeMehDown.on_message(filters.command("start"))
async def start_message(bot, message):
         button = [[
            InlineKeyboardButton("Dev🕵🏿‍♀️", url="t.me/myself_gon")
            ],[
            InlineKeyboardButton("START", callback_data="start"),
            InlineKeyboardButton("HELP", callback_data="help")
            ],[
            InlineKeyboardButton("ABOUT", callback_data="about"),
            InlineKeyboardButton("INFO", callback_data="info"),
            InlineKeyboardButton("SUPPORT", callback_data="support")
            ]]
         await message.reply_photo(
         photo=random.choice(ALL_PICS),
                  caption=START_MESSAGE.format(message.from_user.menton),
                  reply_markup=InlineKeyboardMarkup(button)
         )


@TakeMehDown.on_callback_query()
async def callback(client: TakeMehDown, query: CallbackQuery):
         if query.data == "start":
               await query.message.edit(
                        text = f"""
Hey {first_name} Wassup!!🤖
""",
                        reply_markup=InlineKeyboardMarkup( [[
                                InlineKeyboardButton("Dev🕵🏿‍♀️", url="t.me/myself_gon")
                                ],[
                                InlineKeyboardButton("START", callback_data="start"),
                                InlineKeyboardButton("HELP", callback_data="help")
                                ],[
                                InlineKeyboardButton("ABOUT", callback_data="about"),
                                InlineKeyboardButton("INFO", callback_data="info"),
                                InlineKeyboardButton("SUPPORT", callback_data="support")
                                ]]
                        )
               )
                

         elif query.data == "help":
               await msg.message.edit(
                        text = """
👶🏿what the fuck do you want!!? its mine sucker💢
""",
                        reply_markup=InlineKeyboardMarkup( [[
                                InlineKeyboardButton("start", callback_data="start")
                                ]]
                        )
                       
               )

         elif query.data == "about":
               await msg.message.edit(
                        text = """
💤what are you looking type /info or click info button💘
""",
                        reply_markup=InlineKeyboardMarkup( [[
                                InlineKeyboardButton("start", callback_data="start")
                                ]]
                        )
               )



         elif query.data == "info":
               await msg.message.edit(
                        text = f"""
🤵🏿First Name - {msg.from_user.first_name}
👨🏿‍💻Last Name - {msg.from_user.last_name}
🕳Usrname - {msg.from_user.username} 
🌐Id - {msg.from_user.id}
〽Mention - {msg.from_user.mention}
    O_O @myself_gon""",
                        reply_markup=InlineKeyboardMarkup( [[
                                InlineKeyboardButton("start", callback_data="start")
                                ]]
                        )

               )


         elif query.data == "support":
               await msg.message.edit(
                        text = """
Support meh by joining 
 @TakeMehDown
""",
                        reply_markup=InlineKeyboardMarkup( [[
                                InlineKeyboardButton("start", callback_data="start")
                                ]]
                        )

               )
                                    


@TakeMehDown.on_message(filters.command("info"))
async def info(bot, msg):
         text = f"""
🤵🏿First Name - {msg.from_user.first_name}
👨🏿‍💻Last Name - {msg.from_user.last_name}
🕳Usrname - {msg.from_user.username} 
🌐Id - {msg.from_user.id}
〽Mention - {msg.from_user.mention}"""


        await msg.reply_text(text=text)


  
TakeMehDown.run()
