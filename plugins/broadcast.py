# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

from pyrogram import Client, filters
import datetime
import time
from database.users_chats_db import db
from info import ADMINS
from utils import broadcast_messages, broadcast_messages_group
import asyncio

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

@Client.on_message(filters.command("broadcast") & filters.user(ADMINS) & filters.reply)
async def verupikkals(bot, message):
    users = await db.get_all_users()
    b_msg = message.reply_to_message
    sts = await message.reply_text(
        text='Bʀᴏᴀᴅᴄᴀsᴛɪɴɢ Yᴏᴜʀ Mᴇssᴀɢᴇs...'
    )
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    blocked = 0
    deleted = 0
    failed =0

    success = 0
    async for user in users:
        pti, sh = await broadcast_messages(int(user['id']), b_msg)
        if pti:
            success += 1
        elif pti == False:
            if sh == "Blocked":
                blocked+=1
            elif sh == "Deleted":
                deleted += 1
            elif sh == "Error":
                failed += 1
        done += 1
        await asyncio.sleep(2)
        if not done % 20:
            await sts.edit(f"Bʀᴏᴀᴅᴄᴀsᴛ Iɴ Pʀᴏɢʀᴇss:\n\nTᴏᴛᴀʟ Usᴇʀs: {total_users}\nCᴏᴍᴘʟᴇᴛᴇᴅ: {done} / {total_users}\nSᴜᴄᴄᴇss: {success}\nBʟᴏᴄᴋᴇᴅ: {blocked}\nDᴇʟᴇᴛᴇᴅ: {deleted}")    
    time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
    await sts.edit(f"Bʀᴏᴀᴅᴄᴀsᴛ Cᴏᴍᴘʟᴇᴛᴇᴅ:\nCᴏᴍᴘʟᴇᴛᴇᴅ Iɴ {time_taken} Sᴇᴄᴏɴᴅs.\n\nTᴏᴛᴀʟ Usᴇʀs {total_users}\nCᴏᴍᴘʟᴇᴛᴇᴅ: {done} / {total_users}\nSᴜᴄᴄᴇss: {success}\nBʟᴏᴄᴋᴇᴅ: {blocked}\nDᴇʟᴇᴛᴇᴅ: {deleted}")

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #

@Client.on_message(filters.command("group_broadcast") & filters.user(ADMINS) & filters.reply)
async def broadcast_group(bot, message):
    groups = await db.get_all_chats()
    b_msg = message.reply_to_message
    sts = await message.reply_text(
        text='Bʀᴏᴀᴅᴄᴀsᴛɪɴɢ Yᴏᴜʀ Mᴇssᴀɢᴇs Tᴏ Gʀᴏᴜᴘs...'
    )
    start_time = time.time()
    total_groups = await db.total_chat_count()
    done = 0
    failed =0

    success = 0
    async for group in groups:
        pti, sh = await broadcast_messages_group(int(group['id']), b_msg)
        if pti:
            success += 1
        elif sh == "Error":
                failed += 1
        done += 1
        if not done % 20:
            await sts.edit(f"Bʀᴏᴀᴅᴄᴀsᴛ Iɴ Pʀᴏɢʀᴇss:\n\nTᴏᴛᴀʟ Gʀᴏᴜᴘs {total_groups}\nCᴏᴍᴘʟᴇᴛᴇᴅ: {done} / {total_groups}\nSᴜᴄᴄᴇss: {success}")    
    time_taken = datetime.timedelta(seconds=int(time.time()-start_time))
    await sts.edit(f"Bʀᴏᴀᴅᴄᴀsᴛ Cᴏᴍᴘʟᴇᴛᴇᴅ:\nCᴏᴍᴘʟᴇᴛᴇᴅ Iɴ {time_taken} Sᴇᴄᴏɴᴅs.\n\nTᴏᴛᴀʟ Gʀᴏᴜᴘs {total_groups}\nCᴏᴍᴘʟᴇᴛᴇᴅ: {done} / {total_groups}\nSᴜᴄᴄᴇss: {success}")

# ------------------------- #
# Don't Remove Credit 
# Ask Doubt @AU_Bot_Discussion 
# Owner @Mr_Mohammed_29 
# ------------------------- #
