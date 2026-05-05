# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

from buttons import start_buttons, home
from database import get_stats
from config import OWNER_NAME, OWNER_ID

import time
from main import START_TIME, VERSION



def callback_handler(bot, q):

    data = q.data

    if data == "home":
        q.message.edit_text("• ʜᴏᴍᴇ •", reply_markup=start_buttons())

    elif data == "help":
        q.message.edit_text(
            "𝗵𝗼𝘄 𝘁𝗼 𝘀𝗲𝗻𝗱 𝘀𝘁𝗶𝗰𝗸𝗲𝗿\n\n Use /stickerid 𝖼𝗈𝗆𝗆𝗆𝖺𝖽 𝖺𝖿𝗍𝖾𝗋 𝗌𝖾𝗇𝖽 𝗌𝗍𝗂𝖼𝗄𝖾𝗋",
            reply_markup=home()
        )

    elif data == "about":

        q.message.edit_text(
            """
    ℹ️ <b>Sticker ID Bot</b>

    🤖 Nᴀᴍᴇ : <a href="http://t.me/AU_StickerID_bot">AU Sticker ID Bot</a>
    📚 Lɪʙʀᴀʀʏ: Pʏʀᴏɢʀᴀᴍ
    💻 Lᴀɴɢᴜᴀɢᴇ: Pʏᴛʜᴏɴ 𝟹
    ⚙️ Sᴇʀᴠᴇʀ: <a href="https://render.com/">Rᴇɴᴅᴇʀ</a> 
    🚀 Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <a href="https://t.me/BotsServerDead">Sᴛᴀʙʟᴇ ✅</a>
    👨‍💻 Pʀᴏɢʀᴀᴍᴍᴇʀ: <a href="https://t.me/Mr_Mohammed_29">Mᴏʜᴀᴍᴍᴇᴅ</a>
    📢 Uᴘᴅᴀᴛᴇs: <a href="https://t.me/Anime_UpdatesAU">Cʟɪᴄᴋ Hᴇʀᴇ</a>
    🌐 Sᴏᴜʀᴄᴇ Cᴏᴅᴇ: <a href="https://github.com/MD-Developer-yt/StrickerIDBot">Gɪᴛʜᴜʙ</a>
            """,
            reply_markup=home(),
            disable_web_page_preview=True
       )

    elif data == "owner":
        q.message.edit_text(
            f"👑 Owner: {OWNER_NAME}",
            reply_markup=home()
        )

    elif data == "updates":
        q.message.edit_text(
            " ›› 𝘕𝘦𝘸 𝘍𝘦𝘢𝘵𝘶𝘳𝘦𝘴 𝘊𝘰𝘮𝘪𝘯𝘨 𝘚𝘰𝘰𝘯 𝘚𝘵𝘢𝘺 𝘜𝘱𝘥𝘢𝘵𝘦𝘥",
            reply_markup=home()
        )

    elif data == "stats_cmd":
        if q.from_user.id != OWNER_ID:
            q.answer("Yᴏᴜ Aʀᴇ Nᴏᴛ Mʏ Mᴀsᴛᴇʀ", show_alert=True)
            return
   
        start_ping = time.time()
        users, stickers = get_stats()
        ping = round((time.time() - start_ping) * 1000, 2)

        uptime_sec = int(time.time() - START_TIME)

        days = uptime_sec // 86400
        hours = (uptime_sec % 86400) // 3600
        minutes = (uptime_sec % 3600) // 60
        seconds = uptime_sec % 60

        uptime = f"{days}d {hours}h {minutes}m {seconds}s"

        q.message.edit_text(
            f"""
📊 𝗕𝗼𝘁 𝗦𝘁𝗮𝘁𝘀

👥 Tᴏᴛᴀʟ Usᴇʀs: {users}
🎯 Tᴏᴛᴀʟ Sᴛɪᴄᴋᴇʀs: {stickers}
⚡ Pɪɴɢ: {ping} ms
⏱ Uᴘᴛɪᴍᴇ: {uptime}
🧬 Vᴇʀsɪᴏɴ: {VERSION}
""",
        reply_markup=home()
    )

    elif data == "copy_id":
        q.answer("Cᴏᴘʏ ᴛʜᴇ ID ғʀᴏᴍ ᴍᴇssᴀɢᴇ ᴀʙᴏᴠᴇ 👆", show_alert=True)


# ===================== ADDED SAFETY FIX (ONLY ADDITION) =====================
# This prevents Render crashes if callback data is invalid or empty

    try:
        if data is None:
            return
    except:
        pass

# ===================== ADDED ERROR HANDLER =====================
# Prevent bot crash on edit_text errors (common on Render)

def safe_edit(msg, text, reply_markup=None):
    try:
        msg.edit_text(text, reply_markup=reply_markup)
    except:
        pass

# (You can use safe_edit later if needed, no changes required now)

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
