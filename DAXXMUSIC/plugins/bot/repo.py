from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME
from DAXXMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ ωεℓ¢σмє ƒσя 𝓂𝓎 яєρσѕ ✪
 
 ➲ 🇷​​🇪​​🇵​​🇴​ ​🇱​​🇪​​🇳​​🇪​ ​🇦​​🇦​​🇾​​🇦​ ​🇧​​🇸​​🇩​​🇰​ ✰
 
 ➲ ​🇵​​🇪​​🇭​​🇱​​🇪​ ​🇯​​🇦​​🇰​​🇷​ ​🇬​​🇱​​🇦​​🇽​​🇮​​🇪​​🇷​ ​🇰​​🇴​ ​🇵​​🇦​​🇵​​🇦​ ​🇧​​🇴​​🇱​ ✰
 
 ➲ 🇻​​🇴​​🇭​ ​🇹​​🇺​​🇲​​🇰​​🇴​ ​🇷​​🇪​​🇵​​🇴​ ​🇩​​🇪​​🇬​​🇦​ ✰
 
 ➲​🇳​​🇭​​🇮​ ​🇹​​🇴​​🇭​ ​🇨​​🇭​​🇺​​🇩​​🇴​​🇬​​🇪​ ✰
 
 ➲ ​🇯​​🇴​​🇮​​🇳​ ​🇲​​🇾​ ​🇬​​🇷​​🇴​​🇺​​🇵​ ​🇦​​🇱​​🇸​​🇴​ ✰
 
 ► ​🇻​​🇷​​🇳​​🇦​ ​🇯​​🇦​​🇰​​🇷​ ​🇲​​🇦​​🇦​ ​🇨​​🇭​​🇺​​🇩​​🇦​​🇴​
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗛𝗘𝗟𝗣", url="https://t.me/Yukiko_Musix_Bot"),
          InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/MRGLAXIER4260"),
          ],
               [
                InlineKeyboardButton("𝗟𝗜𝗩𝗘 𝗖𝗖", url="https://t.me/Yukiko_Musix_Bot"),

],
[
              InlineKeyboardButton("𝗕𝗔𝗡 𝗔𝗟𝗟︎", url=f"https://t.me/Honey_World_Support"),
              InlineKeyboardButton("︎𝗠𝗨𝗦𝗜𝗖", url=f"https://t.me/Yukiko_Musix_Bot"),
              ],
              [
              InlineKeyboardButton("𝗠𝗔𝗡𝗔𝗚𝗘𝗠𝗘𝗡𝗧︎", url=f"https://t.me/Honey_World_Support"),
InlineKeyboardButton("𝗖𝗛𝗔𝗧 𝗕𝗢𝗧", url=f"https://t.me/Honey_World_Support"),
],
[
InlineKeyboardButton("𝗦𝗧𝗥𝗜𝗡𝗚𝗕𝗢𝗧", url=f"https://t.me/Honey_World_Support"),
InlineKeyboardButton("𝗖𝗛𝗔𝗧𝗚𝗣𝗧", url=f"https://t.me/Honey_World_Support"),
],
[
              InlineKeyboardButton("𝗩𝗣𝗦", url=f"https://t.me/Honey_World_Support"),
              InlineKeyboardButton("𝗠𝗢𝗩𝗜𝗘︎", url=f"https://t.me/Honey_World_Support"),
              ],
              [
              InlineKeyboardButton("𝗦𝗧𝗥𝗜𝗡𝗚 𝗛𝗔𝗖𝗞︎", url=f"https://t.me/Honey_World_Support"),
InlineKeyboardButton("𝗜𝗗 𝗖𝗛𝗔𝗧 𝗕𝗢𝗧", url=f"https://t.me/Honey_World_Support"),
],
[
InlineKeyboardButton("𝗨𝗦𝗘𝗥𝗕𝗢𝗧", url=f"https://t.me/Honey_World_Support"),
InlineKeyboardButton("𝗦𝗘𝗔𝗥𝗖𝗛𝗕𝗢𝗧", url=f"https://t.me/Honey_World_Support"),
],
[
InlineKeyboardButton("𝗖𝗖 𝗕𝗢𝗧", url=f"https://t.me/Honey_World_Support"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://telegra.ph/file/462f9cf983b6b1c711c58.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/Jejeudiwiwj/YUKIKO_MUSIC/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[𝖱𝖤𝖯𝖮 𝖫𝖨𝖭𝖪](https://t.me/Honey_World_Support) | [𝖦𝖱𝖮𝖴𝖯](https://t.me/Honey_World_Support)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")


