BOT_TOKEN = "5442822436:AAGXM3QXL1YCfDDdOLDP3-3PrOOWQ5P-Knk"
OPENAI_API = "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"
ZENZ_API = "zenzkey_dac641da2e"
OWNER_ID = 1666509342
GROUP_ID = [-1001838203549]
AUTO_REPLY = "True"

import os, sys, random, time, json, schedule
import requests, telebot, datetime, pytube, openai, pysdbots, catboys
from time import sleep
from telebot import *
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from pytube import *
from catboys import *
from pysdbots import *
from db import *

bot = telebot.TeleBot(BOT_TOKEN, parse_mode='HTML')
openai.api_key = OPENAI_API

hideboard = types.ReplyKeyboardRemove()

users = []
userinfo = {}
admins = [1666509342]

heart_emoji = ["❤", "️🧡", "💛", "💚", "💙", "💜", "🖤", "🤍", "🤎", "❤‍🔥", "❣️", "💕", "💞", "💓", "💗", "💖", "💝"]

def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            if m.chat.type == "private":
                if int(m.chat.id) not in users:
                    users.append(m.from_user.id)
                    userinfo[str(m.from_user.id)] = {"username": str(m.from_user.username), "name": str(m.from_user.first_name), "points": 0}
                    print(users)
                    print(userinfo)
                if int(m.chat.id) != OWNER_ID:
                    text = "👤 Fʀᴏᴍ : @" +str(m.from_user.username)
                    text += "\n💬 Tᴇxᴛ : " +str(m.text)
                    bot.send_message(OWNER_ID, text)
            elif m.chat.type == "group" or m.chat.type == "supergroup":
                if int(m.chat.id) not in GROUP_ID:
                    bot.leave_chat(m.chat.id)

bot.set_update_listener(listener)

@bot.message_handler(content_types=['photo'])
def photo(message):
    print ("message.photo = " +str(message.photo))
    fileID = message.photo[-1].file_id
    print ("fileID = " +fileID)
    file_info = bot.get_file(fileID)
    print ("file.file_path = " +file_info.file_path)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("image.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.send_photo(message.chat.id, "/sdcard/HYDRA-TG-BOT/image.jpg")

@bot.message_handler(commands=["test"])
def command_test(m):
    bot.send_sticker(m.chat.id, "")

#https://github.com/SL-Hydra/HYDRA-TG-BOT
@bot.message_handler(commands=["help", "start"])
def command_help(m):
    if m.from_user.id not in users:
        users.append(m.from_user.id)
        userinfo[str(m.from_user.id)] = {"username": str(m.from_user.username), "points": 0}
        print(users)
        print(userinfo)
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
        join = types.KeyboardButton(text="Joined ✅")
        keyboard.add(join)
        text = "⛔️ You Must Join Our Support Group"
        text += "\n\n  ✅ <a href='t.me/HydraBotSupport'>HYDRA-BOT Support Group</a>"
        text += "\n\n❇️ After Joining, Click On 'Joined ✅'"
        bot.send_message(m.chat.id, text, reply_markup=keyboard)
    else:
        bot.send_chat_action(m.chat.id, 'typing')
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        line = types.InlineKeyboardButton(text="╭═══════🤖═══════╮", callback_data="line")
        menu = types.InlineKeyboardButton(text="|           📜 Mᴇɴᴜ 📜           |", callback_data="menu")
        info = types.InlineKeyboardButton(text="|            🌷 Iɴꜰᴏ 🌷            |", callback_data="info")
        settings = types.InlineKeyboardButton(text="|        ⚙️ Sᴇᴛᴛɪɴɢꜱ ⚙️        |", callback_data="settings")
        #add_me_to_group = types.InlineKeyboardButton(text="➕ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘ ➕", url="http://t.me/SLHydrabot?startgroup=true")
        close_help = types.InlineKeyboardButton(text="|                   🗑                  |️", callback_data="close_help")
        line1 = types.InlineKeyboardButton(text="╰═══════🤖═══════╯", callback_data="line")
        keyboard.add(line)
        keyboard.add(menu)
        keyboard.add(info)
        keyboard.add(settings)
        #keyboard.add(add_me_to_group)
        keyboard.add(close_help)
        keyboard.add(line1)
        logo = ["https://telegra.ph/file/8415f7ada38fbfd70cb1c.jpg", anime_logo("HYDRA BOT")]
        text = "<b>💠 Hᴇʟʟᴏ " +m.from_user.first_name+ " 👋</b>"
        text += "\n<b>Wᴇʟᴄᴏᴍᴇ Tᴏ 𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻</b>"
        text += "\n\n<b>I ᴀᴍ ᴀ Pᴏᴡᴇʀꜰᴜʟ Bᴏᴛ Wɪᴛʜ Cᴏᴏʟ Fᴇᴀᴛᴜʀᴇꜱ 🌝❤️ Aɴᴅ Yᴏᴜ Cᴀɴ Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴘꜱ 👥</b>"
        text += "\n<b>Nᴏᴡ, Eɴᴊᴏʏ! 🤗</b>"
        text += "\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>"
        global help
        help_msg = bot.send_photo(m.chat.id, random.choice(logo), caption=text, reply_markup=keyboard)

@bot.message_handler(commands=["menu", "panel", "list"])
def command_menu(m):
    text = "<b>👥 📜 𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 COMMAND LIST 📜</b>\n"
    text += "\n𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 Commands are classified into 7 categories 🗒️\n"
    text += "\nSelect your choice ⤵️"
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    all_menu = types.InlineKeyboardButton(text="Aʟʟ Cᴏᴍᴍᴀɴᴅꜱ", callback_data="all_menu")
    main_menu = types.InlineKeyboardButton(text="Mᴀɪɴ Cᴏᴍᴍᴀɴᴅꜱ", callback_data="main_menu")
    search_menu = types.InlineKeyboardButton(text="Sᴇᴀʀᴄʜ Cᴏᴍᴍᴀɴᴅꜱ", callback_data="search_menu")
    image_menu = types.InlineKeyboardButton(text="Iᴍᴀɢᴇ Cᴏᴍᴍᴀɴᴅꜱ", callback_data="image_menu")
    information_menu = types.InlineKeyboardButton(text="Iɪɴꜰᴏʀᴍᴀᴛɪᴏɴ Cᴏᴍᴍᴀɴᴅꜱ", callback_data="information_menu")
    convert_menu = types.InlineKeyboardButton(text="Cᴏɴᴠᴇʀᴛ Cᴏᴍᴍᴀɴᴅꜱ", callback_data="convert_menu")
    adult_menu = types.InlineKeyboardButton(text="18+ Cᴏᴍᴍᴀɴᴅꜱ", callback_data="adult_menu")
    other_menu = types.InlineKeyboardButton(text="Oᴛʜᴇʀ Cᴏᴍᴍᴀɴᴅꜱ", callback_data="other_menu")
    keyboard.add(all_menu)
    keyboard.add(main_menu)
    keyboard.add(search_menu)
    keyboard.add(image_menu)
    keyboard.add(information_menu)
    keyboard.add(convert_menu)
    keyboard.add(adult_menu)
    keyboard.add(other_menu)
    bot.reply_to(m, text, reply_markup=keyboard)

@bot.message_handler(commands=["all_menu"])
def command_all_menu(m):
    text = "<b>👥 📜𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 ALL MENU📜</b>\n"
    Command_Emojys = ["🔥", "💞", "🔰", "💠", "♦️"]
    Desc_Emojys = ["📖", "📋", "🗒️", "📝", "📃"]
    Usage_Emojys = ["🏷️", "🔖", "✏️", "🖊️", "🔑"]
    cemojy = random.choice(Command_Emojys)
    demojy = random.choice(Desc_Emojys)
    uemojy = random.choice(Usage_Emojys)
    for key in ALL_MENU:
        text += "\n" +cemojy+ " <b>Cᴏᴍᴍᴀɴᴅ :</b> " +key
        text += "\n" +demojy+ " <b>Dᴇꜱᴄʀɪᴘᴛɪᴏɴ :</b> <i>" +ALL_MENU[key][0]+ "</i>"
        text += "\n" +uemojy+ " <b>Usage :</b> <code>" +ALL_MENU[key][1]+ "</code>\n"
    bot.reply_to(m, text)

@bot.message_handler(commands=["main_menu"])
def command_main_menu(m):
    text = "<b>👥 📜𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 MAIN MENU📜</b>\n"
    Command_Emojys = ["🔥", "💞", "🔰", "💠", "♦️"]
    Desc_Emojys = ["📖", "📋", "🗒️", "📝", "📃"]
    Usage_Emojys = ["🏷️", "🔖", "✏️", "🖊️", "🔑"]
    cemojy = random.choice(Command_Emojys)
    demojy = random.choice(Desc_Emojys)
    uemojy = random.choice(Usage_Emojys)
    for key in MAIN_MENU:
        text += "\n" +cemojy+ " <b>Cᴏᴍᴍᴀɴᴅ :</b> " +key
        text += "\n" +demojy+ " <b>Dᴇꜱᴄʀɪᴘᴛɪᴏɴ :</b> <i>" +MAIN_MENU[key][0]+ "</i>"
        text += "\n" +uemojy+ " <b>Usage :</b> <code>" +MAIN_MENU[key][1]+ "</code>\n"
    bot.reply_to(m, text)

@bot.message_handler(commands=["search_menu"])
def command_search_menu(m):
    text = "<b>👥 📜𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 SEARCH MENU📜</b>\n"
    Command_Emojys = ["🔥", "💞", "🔰", "💠", "♦️"]
    Desc_Emojys = ["📖", "📋", "🗒️", "📝", "📃"]
    Usage_Emojys = ["🏷️", "🔖", "✏️", "🖊️", "🔑"]
    cemojy = random.choice(Command_Emojys)
    demojy = random.choice(Desc_Emojys)
    uemojy = random.choice(Usage_Emojys)
    for key in SEARCH_MENU:
        text += "\n" +cemojy+ " <b>Cᴏᴍᴍᴀɴᴅ :</b> " +key
        text += "\n" +demojy+ " <b>Dᴇꜱᴄʀɪᴘᴛɪᴏɴ :</b> <i>" +SEARCH_MENU[key][0]+ "</i>"
        text += "\n" +uemojy+ " <b>Usage :</b> <code>" +SEARCH_MENU[key][1]+ "</code>\n"
    bot.reply_to(m, text)

@bot.message_handler(commands=["image_menu"])
def command_image_menu(m):
    text = "<b>👥 📜𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 IMAGE MENU📜</b>\n"
    Command_Emojys = ["🔥", "💞", "🔰", "💠", "♦️"]
    Desc_Emojys = ["📖", "📋", "🗒️", "📝", "📃"]
    Usage_Emojys = ["🏷️", "🔖", "✏️", "🖊️", "🔑"]
    cemojy = random.choice(Command_Emojys)
    demojy = random.choice(Desc_Emojys)
    uemojy = random.choice(Usage_Emojys)
    for key in IMAGE_MENU:
        text += "\n" +cemojy+ " <b>Cᴏᴍᴍᴀɴᴅ :</b> " +key
        text += "\n" +demojy+ " <b>Dᴇꜱᴄʀɪᴘᴛɪᴏɴ :</b> <i>" +IMAGE_MENU[key][0]+ "</i>"
        text += "\n" +uemojy+ " <b>Usage :</b> <code>" +IMAGE_MENU[key][1]+ "</code>\n"
    bot.reply_to(m, text)

@bot.message_handler(commands=["information_menu"])
def command_information_menu(m):
    text = "<b>👥 📜𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 INFORMATION MENU📜</b>\n"
    Command_Emojys = ["🔥", "💞", "🔰", "💠", "♦️"]
    Desc_Emojys = ["📖", "📋", "🗒️", "📝", "📃"]
    Usage_Emojys = ["🏷️", "🔖", "✏️", "🖊️", "🔑"]
    cemojy = random.choice(Command_Emojys)
    demojy = random.choice(Desc_Emojys)
    uemojy = random.choice(Usage_Emojys)
    for key in INFORMATION_MENU:
        text += "\n" +cemojy+ " <b>Cᴏᴍᴍᴀɴᴅ :</b> " +key
        text += "\n" +demojy+ " <b>Dᴇꜱᴄʀɪᴘᴛɪᴏɴ :</b> <i>" +INFORMATION_MENU[key][0]+ "</i>"
        text += "\n" +uemojy+ " <b>Usage :</b> <code>" +INFORMATION_MENU[key][1]+ "</code>\n"
    bot.reply_to(m, text)

@bot.message_handler(commands=["convert_menu"])
def command_convert_menu(m):
    text = "<b>👥 📜𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 CONVERT MENU📜</b>\n"
    Command_Emojys = ["🔥", "💞", "🔰", "💠", "♦️"]
    Desc_Emojys = ["📖", "📋", "🗒️", "📝", "📃"]
    Usage_Emojys = ["🏷️", "🔖", "✏️", "🖊️", "🔑"]
    cemojy = random.choice(Command_Emojys)
    demojy = random.choice(Desc_Emojys)
    uemojy = random.choice(Usage_Emojys)
    for key in CONVERT_MENU:
        text += "\n" +cemojy+ " <b>Cᴏᴍᴍᴀɴᴅ :</b> " +key
        text += "\n" +demojy+ " <b>Dᴇꜱᴄʀɪᴘᴛɪᴏɴ :</b> <i>" +CONVERT_MENU[key][0]+ "</i>"
        text += "\n" +uemojy+ " <b>Usage :</b> <code>" +CONVERT_MENU[key][1]+ "</code>\n"
    bot.reply_to(m, text)

@bot.message_handler(commands=["adult_menu"])
def command_adult_menu(m):
    text = "<b>👥 📜𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 ADULT MENU📜</b>\n"
    Command_Emojys = ["🔥", "💞", "🔰", "💠", "♦️"]
    Desc_Emojys = ["📖", "📋", "🗒️", "📝", "📃"]
    Usage_Emojys = ["🏷️", "🔖", "✏️", "🖊️", "🔑"]
    cemojy = random.choice(Command_Emojys)
    demojy = random.choice(Desc_Emojys)
    uemojy = random.choice(Usage_Emojys)
    for key in ADULT_MENU:
        text += "\n" +cemojy+ " <b>Cᴏᴍᴍᴀɴᴅ :</b> " +key
        text += "\n" +demojy+ " <b>Dᴇꜱᴄʀɪᴘᴛɪᴏɴ :</b> <i>" +ADULT_MENU[key][0]+ "</i>"
        text += "\n" +uemojy+ " <b>Usage :</b> <code>" +ADULT_MENU[key][1]+ "</code>\n"
    bot.reply_to(m, text)

@bot.message_handler(commands=["other_menu"])
def command_other_menu(m):
    text = "<b>👥 📜𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 OTHER MENU📜</b>\n"
    Command_Emojys = ["🔥", "💞", "🔰", "💠", "♦️"]
    Desc_Emojys = ["📖", "📋", "🗒️", "📝", "📃"]
    Usage_Emojys = ["🏷️", "🔖", "✏️", "🖊️", "🔑"]
    cemojy = random.choice(Command_Emojys)
    demojy = random.choice(Desc_Emojys)
    uemojy = random.choice(Usage_Emojys)
    for key in OTHER_MENU:
        text += "\n" +cemojy+ " <b>Cᴏᴍᴍᴀɴᴅ :</b> " +key
        text += "\n" +demojy+ " <b>Dᴇꜱᴄʀɪᴘᴛɪᴏɴ :</b> <i>" +OTHER_MENU[key][0]+ "</i>"
        text += "\n" +uemojy+ " <b>Usage :</b> <code>" +OTHER_MENU[key][1]+ "</code>\n"
    bot.reply_to(m, text)

@bot.message_handler(commands=["info"])
def command_info(m):
    bot.reply_to(m, INFO, disable_web_page_preview=True)

@bot.message_handler(commands=["anime"])
def command_anime(m):
    if m.text == "/anime":
        bot.reply_to(m, "<b>Wrong command❗</b>\n[<code>/anime your_amount</code>]")
    else:
        text = m.text.replace("/anime ", "")
        wait = bot.reply_to(m, "Please wait....⏳")
        bot.send_chat_action(m.chat.id, 'upload_photo')
        bot.delete_message(chat_id=wait.chat.id, message_id=wait.message_id)
        text = int(text)
        if text <= 20:
            for i in range(text):
                bot.send_photo(m.chat.id, catboys.img())
        else:
            bot.reply_to(m, "<b>Maximum amount is 20❗</b>")

@bot.message_handler(commands=["apod"])
def command_apod(m):
    wait = bot.reply_to(m, "Please wait....⏳")
    API = "https://api.sdbots.tk/apod"
    apod = requests.get(API).json()
    bot.delete_message(chat_id=wait.chat.id, message_id=wait.message_id)
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    view_apod = types.InlineKeyboardButton(text="📖 Vɪᴇᴡ Mᴏʀᴇ 📖", callback_data="view_apod")
    visit_apod = types.InlineKeyboardButton(text="🌐 Vɪꜱɪᴛ Mᴏʀᴇ 🌐", url="https://apod.nasa.gov/apod/")
    keyboard.add(view_apod)
    keyboard.add(visit_apod)
    text = "<b>🌠 Tɪᴛʟᴇ : " +str(apod['title'])+ "</b>"
    text += "\n\n<b><code>📅 " +str(apod['date'])+ "</code></b>"
    bot.send_photo(m.chat.id, str(apod['image']), caption=text, reply_markup=keyboard)

@bot.message_handler(commands=["broadcast"])
def command_broadcast(m):
    if m.text == "/broadcast":
        bot.reply_to(m, "<b>Wrong command❗</b>\n[<code>/broadcast your_text</code>]")
    else:
        text = m.text.replace("/broadcast ", "")
        wait = bot.reply_to(m, "Please wait....⏳")
        bot.delete_message(chat_id=wait.chat.id, message_id=wait.message_id)
        for i in users:
            bot.send_message(i, text)

@bot.message_handler(commands=["fakeinfo"])
def command_fakeinfo(m):
    bot.reply_to(m, "Still Development....⏱️ ")

@bot.message_handler(commands=["fancy"])
def command_fancy(m):
    if m.text == "/fancy":
        bot.reply_to(m, "<b>Wrong command❗</b>\n[<code>/fancy your_text</code>]")
    else:
        text = m.text.replace("/fancy ", "")
        wait = bot.reply_to(m, "Generating your text....⏳")
        API = f"https://api.zahwazein.xyz/searching/styletext?query={text}&apikey={ZENZ_API}"
        fancy = requests.get(API).json()
        bot.delete_message(chat_id=wait.chat.id, message_id=wait.message_id)
        if fancy["status"] == "OK":
            result = fancy.get("result")
            text = "<b>🐉 𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 Fᴀɴᴄʏ Tᴇxᴛ Gᴇɴᴇʀᴀᴛᴇʀ 🐉</b>\n"
            n = 0
            for value in result:
                text += "\n" +result[n]["name"]+ " ➤ <code>" +result[n]["result"]+ "</code>\n"
                n = n+1
            if len(text) > 4095:
                for x in range(0, len(text), 4095):
                    bot.send_message(m.chat.id, text[x:x+4095], disable_web_page_preview=True)
            else:
                bot.reply_to(m, text)
        else:
            bot.reply_to(m, "<b>Can't connect API right now❗</b>")

@bot.message_handler(commands=["gender"])
def command_gender(m):
    if m.text == "/gender":
        bot.reply_to(m, "<b>Wrong command❗</b>\n[<code>/gender your_text</code>]")
    else:
        text = m.text.replace("/gender ", "")
        API = "https://api.genderize.io/?name=" +text
        gender = requests.get(API).json()
        wait = bot.reply_to(m, "Generating....⏳")
        bot.delete_message(chat_id=wait.chat.id, message_id=wait.message_id)
        text = "<b>🐉 𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 Gᴇɴᴅᴇʀ Dᴇᴛᴇᴄᴛᴇʀ 🐉</b>\n"
        text += "\n<b>Gᴇɴᴅᴇʀ ➤</b> <code>" +str(gender["gender"])+ "</code>"
        text += "\n<b>Pʀᴏʙᴀʙɪʟɪᴛʏ ➤</b> <code>" +str(gender["probability"])+ "</code>"
        bot.reply_to(m, text)

@bot.message_handler(commands=["github"])
def command_github(m):
    if m.text == "/github":
        bot.reply_to(m, "<b>Wrong command❗</b>\n[<code>/github your_username</code>]")
    else:
        text = m.text.replace("/github ", "")
        wait = bot.reply_to(m, "Please wait....⏳")
        API = f"https://api.zahwazein.xyz/stalker/github?username={text}&apikey={ZENZ_API}"
        github = requests.get(API).json()
        bot.delete_message(chat_id=wait.chat.id, message_id=wait.message_id)
        if github["status"] == "OK":
            result = github.get("result")
            text = "<b>🐉 𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 Gɪᴛʜᴜʙ Sᴇᴀʀᴄʜᴇʀ 🐉</b>\n"
            text += "\n<b>👤 Uꜱᴇʀɴᴀᴍᴇ :</b> " +str(result["login"])
            text += "\n<b>📛 Nᴀᴍᴇ :</b> " +str(result["name"])
            text += "\n<b>🛒 Cᴏᴍᴘᴀɴʏ Nᴀᴍᴇ :</b> " +str(result["company"])
            text += "\n<b>🔮 Bʟᴏɢ :</b> " +str(result["blog"])
            text += "\n<b>📍 Lᴏᴄᴀᴛɪᴏɴ :</b> " +str(result["location"])
            text += "\n<b>📩 E-ᴍᴀɪʟ :</b> " +str(result["email"])
            text += "\n<b>🔖 Bɪᴏ :</b> " +str(result["bio"])
            text += "\n\n<b>📢 Pᴜʙʟɪᴄ Rᴇᴘᴏꜱ :</b> " +str(result["public_repos"])
            text += "\n<b>📣 Pᴜʙʟɪᴄ Gɪꜱᴛꜱ :</b> " +str(result["public_gists"])
            text += "\n\n<b>💞 Fᴏʟʟᴏᴡᴇʀꜱ :</b> " +str(result["followers"])
            text += "\n<b>💓 Fᴏʟʟᴏᴡɪɴɢ :</b> " +str(result["following"])
            text += "\n\n<b>📅 Cʀᴇᴀᴛᴇᴅ :</b> " +str(result["created_at"])
            text += "<b>📆 Lᴀꜱᴛ Uᴘᴅᴀᴛᴇᴅ :</b> " +str(result["updated_at"])
            if len(text) > 4095:
                for x in range(0, len(text), 4095):
                    bot.send_message(m.chat.id, text[x:x+4095], disable_web_page_preview=True)
            else:
                bot.reply_to(m, text, disable_web_page_preview=True)
        else:
            bot.reply_to(m, "<b>Can't connect API right now❗</b>")

@bot.message_handler(commands=["id"])
def command_id(m):
    bot.reply_to(m, "<b>User ID</b> ➤ <code>" +str(m.chat.id)+ "</code>")

@bot.message_handler(commands=["imagine"])
def command_imagine(m):
    if m.text == "/imagine":
        bot.reply_to(m, "<b>Wrong command❗</b>\n[<code>/imagine your_text</code>]")
    else:
        text = m.text.replace("/imagine ", "")
        wait = bot.reply_to(m, "Please wait....⏳")
        image_resp = openai.Image.create(prompt=text, n=5, size="1024x1024")
        a = image_resp.get("data")
        bot.delete_message(chat_id=wait.chat.id, message_id=wait.message_id)
        bot.send_chat_action(m.chat.id, 'upload_photo')
        for i in range(5):
            bot.send_photo(m.chat.id, a[i]["url"])

@bot.message_handler(commands=["img"])
def command_img(m):
    if m.text == "/img":
        bot.reply_to(m, "<b>Wrong command❗</b>\n[<code>/img your_text</code>]")
    else:
        text = m.text.replace("/img ", "")
        wait = bot.reply_to(m, "Please wait....⏳")
        API = f"https://api.zahwazein.xyz/searching/gimage?query={text}&apikey={ZENZ_API}"
        img = requests.get(API).json()
        bot.send_chat_action(m.chat.id, 'upload_photo')
        bot.delete_message(chat_id=wait.chat.id, message_id=wait.message_id)
        if img["status"] == "OK":
            result = img.get("result")
            n = 0
            for i in range(5):
                bot.send_photo(m.chat.id, result[n])
                n = n+1
        else:
            bot.reply_to(m, "<b>Can't connect API right now❗</b>")

@bot.message_handler(commands=["ip"])
def command_ip(m):
    if m.text == "/ip":
        bot.reply_to(m, "<b>Wrong command❗</b>\n[<code>/ip your_ip</code>]")
    else:
        text = m.text.replace("/ip ", "")
        wait = bot.reply_to(m, "Please wait....⏳")
        API = "https://api.sdbots.tk/ipinfo?ip=" +text
        ip = requests.get(API).json()
        bot.delete_message(chat_id=wait.chat.id, message_id=wait.message_id)
        text = "<b>🐉 𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 Iᴘ Sᴇᴀʀᴄʜᴇʀ 🐉</b>\n"
        text += "\n<b>❐ Iᴘ :</b> <code>" +str(ip["query"])+ "</code>"
        text += "\n<b>❐ Cɪᴛʏ :</b> " +str(ip["city"])
        text += "\n<b>❐ Cᴏᴜɴᴛʀʏ :</b> " +str(ip["country"])
        text += "\n<b>❐ Cᴏᴜɴᴛʀʏ Cᴏᴅᴇ :</b> <code>" +str(ip["countryCode"])+ "</code>"
        text += "\n<b>❐ Aꜱ :</b> " +str(ip["as"])
        text += "\n<b>❐ Iꜱᴘ :</b> " +str(ip["isp"])
        text += "\n<b>❐ Lᴀᴛ :</b> " +str(ip["lat"])
        text += "\n<b>❐ Lᴏɴ :</b> " +str(ip["lon"])
        text += "\n<b>❐ Oʀɢ :</b> " +str(ip["org"])
        text += "\n<b>❐ Rᴇɢɪᴏɴ :</b> " +str(ip["regionName"])
        text += "\n<b>❐ Tɪᴍᴇ Zᴏɴᴇ :</b> " +str(ip["timezone"])
        text += "\n<b>❐ Zɪᴘ :</b> " +str(ip["zip"])
        bot.reply_to(m, text)

@bot.message_handler(commands=["joke"])
def command_joke(m):
    wait = bot.reply_to(m, "Please wait....⏳")
    API = "https://official-joke-api.appspot.com/jokes/random"
    joke = requests.get(API).json()
    bot.delete_message(chat_id=wait.chat.id, message_id=wait.message_id)
    text = "<b>❓ Qᴜᴇꜱᴛɪᴏɴ :</b> " +str(joke["setup"])
    text += "\n\n<b>🟰 Aɴꜱᴡᴇʀ :</b> " +str(joke["punchline"])
    bot.reply_to(m, text)

@bot.message_handler(commands=["langdetect"])
def command_langdetect(m):
    if m.text == "/langdetect":
        bot.reply_to(m, "<b>Wrong command❗</b>\n[<code>/langdetect your_text</code>]")
    else:
        text = m.text.replace("/langdetect ", "")
        API = "https://api.sdbots.tk/detect?text=" +text
        req = requests.get(API).json()
        wait = bot.reply_to(m, "Generating....⏳")
        bot.delete_message(chat_id=wait.chat.id, message_id=wait.message_id)
        text = "<b>🐉 𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 Lᴀɴɢᴜᴀɢᴇ Dᴇᴛᴇᴄᴛᴇʀ 🐉</b>\n"
        text += "\n<b>Lᴀɴɢᴜᴀɢᴇ ➤</b> <code>" +str(req['lang'])+ "</code>"
        bot.reply_to(m, text)

@bot.message_handler(commands=["logoA"])
def command_logoA(m):
    if m.text == "/logoA":
        bot.reply_to(m, "<b>Wrong command❗</b>\n[<code>/logoA your_text</code>]")
    else:
        global logoA_text
        logoA_text = m.text.replace("/logoA ", "")
        wait = bot.reply_to(m, "Please wait....⏳")
        sleep(1)
        bot.delete_message(chat_id=wait.chat.id, message_id=wait.message_id)
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(types.InlineKeyboardButton(text="🇦🇸 American-Flag 🇦🇸", callback_data="American-Flag"), types.InlineKeyboardButton(text="🎴 Anime 🎴", callback_data="Anime"))
        keyboard.add(types.InlineKeyboardButton(text="Awan", callback_data="Awan"), types.InlineKeyboardButton(text="🏖️ Beach 🏖️", callback_data="Beach"))
        keyboard.add(types.InlineKeyboardButton(text="🫐 Berry 🫐", callback_data="Berry"), types.InlineKeyboardButton(text="🖤 Black-Pink 🖤", callback_data="Black-Pink"))
        keyboard.add(types.InlineKeyboardButton(text="💾 Blue-Circuit 💾", callback_data="Blue-Circuit"), types.InlineKeyboardButton(text="Bohlam", callback_data="Bohlam"))
        keyboard.add(types.InlineKeyboardButton(text="🎂 Cake 🎂", callback_data="Cake"), types.InlineKeyboardButton(text="Coklat", callback_data="Coklat"))
        keyboard.add(types.InlineKeyboardButton(text="🎄 Christmas 🎄", callback_data="Christmas"), types.InlineKeyboardButton(text="🪨 Cracked-Stone 🪨", callback_data="Cracked-Stone"))
        keyboard.add(types.InlineKeyboardButton(text="Cross-Fire", callback_data="Cross-Fire"), types.InlineKeyboardButton(text="🐶 Cute-Puppy 🐶", callback_data="Cute-Puppy"))
        keyboard.add(types.InlineKeyboardButton(text="💧 Drop-Water 💧", callback_data="Drop-Water"), types.InlineKeyboardButton(text="Fiction", callback_data="Fiction"))
        keyboard.add(types.InlineKeyboardButton(text="🎇 Firework 🎇", callback_data="Firework"), types.InlineKeyboardButton(text="🔦 Flash-Light 🔦", callback_data="Flash-Light"))
        keyboard.add(types.InlineKeyboardButton(text="🌷 Flower 🌷", callback_data="Flower"), types.InlineKeyboardButton(text="🌁 Foggy-Windows 🌁", callback_data="Foggy-Windows"))
        keyboard.add(types.InlineKeyboardButton(text="🔫 FreeFire-Cover 🔫", callback_data="FreeFire-Cover"), types.InlineKeyboardButton(text="🌌 Galaxy 🌌", callback_data="Galaxy"))
        keyboard.add(types.InlineKeyboardButton(text="🎮 Gaming 🎮", callback_data="Gaming"), types.InlineKeyboardButton(text="🙎 Girl 🙎", callback_data="Girl"))
        keyboard.add(types.InlineKeyboardButton(text="🥛 Glass 🥛", callback_data="Glass"), types.InlineKeyboardButton(text="Glitch", callback_data="Glitch"))
        keyboard.add(types.InlineKeyboardButton(text="Glue", callback_data="Glue"), types.InlineKeyboardButton(text="🪙 Gold 🪙", callback_data="Gold"))
        keyboard.add(types.InlineKeyboardButton(text="Grafity", callback_data="Grafity"), types.InlineKeyboardButton(text="Green-Horror", callback_data="Green-Horror"))
        keyboard.add(types.InlineKeyboardButton(text="🎃 Halloween 🎃", callback_data="Halloween"), types.InlineKeyboardButton(text="🪄 Harry-Potter 🪄", callback_data="Harry-Potter"))
        keyboard.add(types.InlineKeyboardButton(text="Kaligrafi", callback_data="Kaligrafi"), types.InlineKeyboardButton(text="Logo", callback_data="Logo"))
        keyboard.add(types.InlineKeyboardButton(text="Magma", callback_data="Magma"), types.InlineKeyboardButton(text="Marmer", callback_data="Marmer"))
        keyboard.add(types.InlineKeyboardButton(text="Matrix", callback_data="Matrix"), types.InlineKeyboardButton(text="Metallic", callback_data="Metallic"))
        keyboard.add(types.InlineKeyboardButton(text="☪️ Muslim-Semi ☪️", callback_data="Muslim-Semi"), types.InlineKeyboardButton(text="🌳 Natural 🌳", callback_data="Natural"))
        keyboard.add(types.InlineKeyboardButton(text="Neon", callback_data="Neon"), types.InlineKeyboardButton(text="👹 Neon-Devil 👹", callback_data="Neon-Devil"))
        keyboard.add(types.InlineKeyboardButton(text="💬 Quotes 💬", callback_data="Quotes"), types.InlineKeyboardButton(text="💎 Ruby 💎", callback_data="Ruby"))
        keyboard.add(types.InlineKeyboardButton(text="👤 Shadow 👤", callback_data="Shadow"), types.InlineKeyboardButton(text="Sketch", callback_data="Sketch"))
        keyboard.add(types.InlineKeyboardButton(text="☄️ Space ☄️", callback_data="Space"), types.InlineKeyboardButton(text="🕷️ Spider 🕷️", callback_data="Spider"))
        keyboard.add(types.InlineKeyboardButton(text="🌟 Star 🌟", callback_data="Star"), types.InlineKeyboardButton(text="🌠 Star-Night 🌠", callback_data="Star-Night"))
        keyboard.add(types.InlineKeyboardButton(text="⚡ Thunder ⚡", callback_data="Thunder"), types.InlineKeyboardButton(text="Transformer", callback_data="Transformer"))
        keyboard.add(types.InlineKeyboardButton(text="🌅 Wallpaper 🌅", callback_data="Wallpaper"), types.InlineKeyboardButton(text="✍️ Write ✍️", callback_data="Write"))
        keyboard.add(types.InlineKeyboardButton(text="Yasuo", callback_data="Yasuo"), types.InlineKeyboardButton(text="Other", callback_data="Other"))
        text = "<b>🐉 𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 Lᴏɢᴏ Gᴇɴᴇʀᴀᴛᴇʀ v1🐉</b>\n"
        text += "\n💬 Tᴇxᴛ : <code>" +logoA_text+ "</code>\n"
        text += "\n<b>Select your logo ⤵️</b>"
        bot.reply_to(m, text, reply_markup=keyboard)

@bot.message_handler(commands=["logoB"])
def command_logoB(m):
    if m.text == "/logoB":
        bot.reply_to(m, "<b>Wrong command❗</b>\n[<code>/logoB text1:text2</code>]")
    elif ":" not in m.text:
        bot.reply_to(m, "<b>You must use ' <code>:</code> '❗</b>\n[<code>/logoB text1:text2</code>]")
    else:
        logo_text = m.text.replace("/logoB ", "")
        global logoB_text
        logoB_text = logo_text.split(':')
        wait = bot.reply_to(m, "Please wait....⏳")
        sleep(1)
        bot.delete_message(chat_id=wait.chat.id, message_id=wait.message_id)
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(types.InlineKeyboardButton(text="Glitch", callback_data="Glitch1"), types.InlineKeyboardButton(text="🦸‍♂️ Marval 🦸‍♂️", callback_data="Marval"))
        keyboard.add(types.InlineKeyboardButton(text="Piring-Kaligrafi", callback_data="Piring-Kaligrafi"), types.InlineKeyboardButton(text="💋 Pornhub 💋", callback_data="Pornhub"))
        keyboard.add(types.InlineKeyboardButton(text="💬 Quotes 💬", callback_data="Quotes1"), types.InlineKeyboardButton(text="Sparkling", callback_data="Sparkling"))
        keyboard.add(types.InlineKeyboardButton(text="Typography", callback_data="Typography"), types.InlineKeyboardButton(text="🐺 Wolf 🐺", callback_data="Wolf"))
        text = "<b>🐉 𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 Lᴏɢᴏ Gᴇɴᴇʀᴀᴛᴇʀ v2🐉</b>\n"
        text += "\n💬 Tᴇxᴛ 1 : <code>" +logoB_text[0]+ "</code>"
        text += "\n💬 Tᴇxᴛ 2 : <code>" +logoB_text[1]+ "</code>\n"
        text += "\n<b>Select your logo ⤵️</b>"
        bot.reply_to(m, text, reply_markup=keyboard)

@bot.message_handler(commands=["logoC"])
def command_logoC(m):
    if m.text == "/logoC":
        bot.reply_to(m, "<b>Wrong command❗</b>\n[<code>/logoC text1:text2:text3</code>]")
    elif ":" not in m.text:
        bot.reply_to(m, "<b>You must use ' <code>:</code> '❗</b>\n[<code>/logoC text1:text2:text3</code>]")
    else:
        logo_text = m.text.replace("/logoC ", "")
        global logoC_text
        logoC_text = logo_text.split(':')
        if len(logoC_text) > 2:
            wait = bot.reply_to(m, "Please wait....⏳")
            sleep(1)
            bot.delete_message(chat_id=wait.chat.id, message_id=wait.message_id)
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            keyboard.add(types.InlineKeyboardButton(text="Pro-Yector", callback_data="Pro-Yector"), types.InlineKeyboardButton(text="Valorant", callback_data="Valorant"))
            text = "<b>🐉 𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 Lᴏɢᴏ Gᴇɴᴇʀᴀᴛᴇʀ v3🐉</b>\n"
            text += "\n💬 Tᴇxᴛ 1 : <code>" +logoC_text[0]+ "</code>"
            text += "\n💬 Tᴇxᴛ 2 : <code>" +logoC_text[1]+ "</code>"
            text += "\n💬 Tᴇxᴛ 3 : <code>" +logoC_text[2]+ "</code>\n"
            text += "\n<b>Select your logo ⤵️</b>"
            bot.reply_to(m, text, reply_markup=keyboard)
        else:
            bot.reply_to(m, "<b>You must use ' <code>:</code> '❗</b>\n[<code>/logoC text1:text2:text3</code>]")

@bot.message_handler(commands=["logo3D"])
def command_logo3D(m):
    if m.text == "/logo3D":
        bot.reply_to(m, "<b>Wrong command❗</b>\n[<code>/logo3D your_text</code>]")
    else:
        global logo3D_text
        logo3D_text = m.text.replace("/logo3D ", "")
        wait = bot.reply_to(m, "Please wait....⏳")
        sleep(1)
        bot.delete_message(chat_id=wait.chat.id, message_id=wait.message_id)
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        keyboard.add(types.InlineKeyboardButton(text="🎄 Christmas 🎄", callback_data="Christmas1"), types.InlineKeyboardButton(text="🌊 Deep-Sea 🌊", callback_data="Deep-Sea"))
        keyboard.add(types.InlineKeyboardButton(text="Gradient", callback_data="Gradient"), types.InlineKeyboardButton(text="Neon-Light", callback_data="Neon-Light"))
        keyboard.add(types.InlineKeyboardButton(text="🌈 Rainbow 🌈", callback_data="Rainbow"), types.InlineKeyboardButton(text="Scifi", callback_data="Scifi"))
        keyboard.add(types.InlineKeyboardButton(text="🚰 Water-Pipe 🚰", callback_data="Water-Pipe"))
        text = "<b>🐉 𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 3D Lᴏɢᴏ Gᴇɴᴇʀᴀᴛᴇʀ v1🐉</b>\n"
        text += "\n💬 Tᴇxᴛ : <code>" +logo3D_text+ "</code>\n"
        text += "\n<b>Select your logo ⤵️</b>"
        bot.reply_to(m, text, reply_markup=keyboard)

@bot.message_handler(commands=["lyrics"])
def command_lyrics(m):
    if m.text == "/lyrics":
        bot.reply_to(m, "<b>Wrong command❗</b>\n[<code>/lyrics song_name</code>]")
    else:
        text = m.text.replace("/lyrics ", "")
        API = "https://api.sdbots.tk/lyrics?song=" +text
        lyrics = requests.get(API).json()
        wait = bot.reply_to(m, "Please wait....⏳")
        bot.delete_message(chat_id=wait.chat.id, message_id=wait.message_id)
        text = "<b>🐉 𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 Lʏʀɪᴄꜱ Sᴇᴀʀᴄʜᴇʀ 🐉</b>"
        text += "\n\n<b>🎶 Sᴏɴɢ Nᴀᴍᴇ : " +str(lyrics['title'])+ "</b>"
        text += "\n<b>🎙️ Aʀᴛɪꜱᴛ :</b> " +str(lyrics['artist'])
        text += "\n\n<b>📖 Lʏʀɪᴄꜱ :</b>\n<code>" +str(lyrics['lyrics'])+ "</code>"
        if len(text) > 4095:
            for x in range(0, len(text), 4095):
                bot.send_message(m.chat.id, text[x:x+4095])
        else:
            bot.reply_to(m, text)

@bot.message_handler(commands=["mediafire"])
def command_mediafire(m):
    if m.text == "/mediafire":
        bot.reply_to(m, "<b>Wrong command❗</b>\n[<code>/mediafire your_link</code>]")
    else:
        bot.reply_to(m, "Still Development....⏱️")

@bot.message_handler(commands=["movie"])
def command_movie(m):
    if m.text == "/movie":
        bot.reply_to(m, "<b>Wrong command❗</b>\n[<code>/movie your_text</code>]")
    else:
        text = m.text.replace("/movie ", "")
        wait = bot.reply_to(m, "Please wait....⏳")
        API = f"https://api.zahwazein.xyz/webzone/imdb?query={text}&apikey={ZENZ_API}"
        movie = requests.get(API).json()
        bot.delete_message(chat_id=wait.chat.id, message_id=wait.message_id)
        if movie["status"] == "OK":
            result = movie.get("result")
            text = "<b>🐉 𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 Mᴏᴠɪᴇ Sᴇᴀʀᴄʜᴇʀ 🐉</b>\n"
            text += "\n<b>Tɪᴛʟᴇ :</b> " +str(result["title"])
            text += "\n<b>Rᴇʟᴇᴀꜱᴇ Dᴀᴛᴇ :</b> " +str(result["released"])
            text += "\n<b>Rᴜɴᴛɪᴍᴇ :</b> " +str(result["runtime"])
            text += "\n<b>Gᴇɴʀᴇꜱ :</b> " +str(result["genres"])
            text += "\n<b>Dɪʀᴇᴄᴛᴏʀ :</b> " +str(result["director"])
            text += "\n<b>Wʀɪᴛᴇʀ :</b> " +str(result["writer"])
            text += "\n<b>Aᴄᴛᴏʀꜱ :</b> " +str(result["actors"])
            text += "\n<b>Lᴀɴɢᴜᴀɢᴇ :</b> " +str(result["language"])
            text += "\n<b>Cᴏᴜɴᴛʀʏ :</b> " +str(result["country"])
            text += "\n<b>Aᴡᴀʀᴅꜱ :</b> " +str(result["awards"])
            text += "\n<b>Rᴀᴛɪɴɢꜱ :</b> " +str(result["rating"])
            text += "\n<b>Vᴏᴛᴇꜱ :</b> " +str(result["votes"])
            keyboard = types.InlineKeyboardMarkup(row_width=2)
            imdb = types.InlineKeyboardButton(text="Visit On IMDB", url=str(result["imdburl"]))
            keyboard.add(imdb)
            bot.send_photo(m.chat.id, str(result["poster"]), caption=text, reply_markup=keyboard)
        else:
            bot.reply_to(m, "<b>Can't connect API right now❗</b>")

@bot.message_handler(commands=["news"])
def command_news(m):
    wait = bot.reply_to(m, "Please wait....⏳")
    API = "https://api.sdbots.tk/hirunews"
    hirunews = requests.get(API).json()
    bot.delete_message(chat_id=wait.chat.id, message_id=wait.message_id)
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    view_news = types.InlineKeyboardButton(text="📰 Vɪᴇᴡ Nᴇᴡꜱ 📰", callback_data="view_news")
    visit_news = types.InlineKeyboardButton(text="🌐 Vɪꜱɪᴛ Mᴏʀᴇ 🌐", url=str(hirunews['link']))
    keyboard.add(view_news)
    keyboard.add(visit_news)
    text = "<b>🗞️ Tɪᴛʟᴇ : " +str(hirunews['title'])+ "</b>"
    text += "\n\n<b><code>📅 " +str(hirunews['date'])+ "</code></b>"
    bot.send_photo(m.chat.id, str(hirunews['img']), caption=text, reply_markup=keyboard)

@bot.message_handler(commands=["ps"])
def command_playstore(m):
    if m.text == "/playstore":
        bot.reply_to(m, "<b>Wrong command❗</b>\n[<code>/playstore your_link</code>]")
    else:
        bot.reply_to(m, "Still Development....⏱️")

@bot.message_handler(commands=["quote"])
def command_quote(m):
    wait = bot.reply_to(m, "Please wait....⏳")
    API = "https://api.quotable.io/random"
    quote = requests.get(API).json()
    bot.delete_message(chat_id=wait.chat.id, message_id=wait.message_id)
    text = "<b>" +str(quote["content"])+ "</b>"
    text += "\n<i>" +str(quote["author"])+ "</i>"
    bot.reply_to(m, text)

@bot.message_handler(commands=["qr"])
def command_qr(m):
    if m.text == "/qr":
        bot.reply_to(m, "<b>Wrong command❗</b>\n[<code>/qr your_text</code>]")
    else:
        text = m.text.replace("/qr ", "")
        wait = bot.reply_to(m, "Generating your image....⏳")
        bot.send_chat_action(m.chat.id, 'upload_photo')
        bot.delete_message(chat_id=wait.chat.id, message_id=wait.message_id)
        bot.send_photo(m.chat.id, "https://apis.xditya.me/qr/gen?text=" +text, caption="<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")

@bot.message_handler(commands=["removebg"])
def command_removebg(m):
    bot.reply_to(m, "Still Development....⏱️")

@bot.message_handler(commands=["shorturl"])
def command_shorturl(m):
    if m.text == "/shorturl":
        bot.reply_to(m, "<b>Wrong command❗</b>\n[<code>/shorturl your_link</code>]")
    else:
        text = m.text.replace("/shorturl ", "")
        wait = bot.reply_to(m, "Generating your URL....⏳")
        API = f"https://api.zahwazein.xyz/convert/shorturl?url={text}&apikey={ZENZ_API}"
        shorturl = requests.get(API).json()
        bot.delete_message(chat_id=wait.chat.id, message_id=wait.message_id)
        if shorturl["status"] == "OK":
            result = shorturl.get("result")
            bot.reply_to(m, "<b>Long URL ➤</b> " +text+ "\n<b>Short URL ➤</b> " +str(result), disable_web_page_preview=True)
        else:
            bot.reply_to(m, "<b>Can't connect API right now❗</b>")

@bot.message_handler(commands=["tiktok"])
def command_tiktok(m):
    if m.text == "/tiktok":
        bot.reply_to(m, "<b>Wrong command❗</b>\n[<code>/tiktok your_link</code>]")
    else:
        bot.reply_to(m, "Still Development....⏱️ ")

@bot.message_handler(commands=["voice"])
def command_voice(m):
    if m.text == "/voice":
        bot.reply_to(m, "<b>Wrong command❗</b>\n[<code>/voice your_text</code>]")
    else:
        text = m.text.replace("/voice ", "")
        wait = bot.reply_to(m, "Please wait....⏳")
        sleep(1)
        bot.delete_message(chat_id=wait.chat.id, message_id=wait.message_id)
        bot.send_voice(m.chat.id, f"http://api.voicerss.org/?key=fcde57f57f864f6f8d74baf4ae7aba23&hl=en-us&c=MP3&f=16khz_16bit_stereo&src={text}")

@bot.message_handler(commands=["wagroup"])
def command_wagroup(m):
    if m.text == "/wagroup":
        bot.reply_to(m, "<b>Wrong command❗</b>\n[<code>/wagroup your_text</code>]")
    else:
        text = m.text.replace("/wagroup ", "")
        wait = bot.reply_to(m, "Please wait....⏳")
        API = f"https://api.zahwazein.xyz/searching/wagroup?query={text}&apikey={ZENZ_API}"
        wagroup = requests.get(API).json()
        bot.delete_message(chat_id=wait.chat.id, message_id=wait.message_id)
        if wagroup["status"] == "OK":
            result = wagroup.get("result")
            text = "<b>🐉 𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 Wʜᴀᴛꜱᴀᴘᴘ Gʀᴏᴜᴘ Sᴇᴀʀᴄʜᴇʀ 🐉</b>\n"
            n = 0
            for value in result:
                text += "\n<b>➤ <a href='" +result[n]["link"]+ "'>" +result[n]["nama"]+ "</a></b>\n"
                n = n+1
            bot.reply_to(m, text)
        else:
            bot.reply_to(m, "<b>Can't connect API right now❗</b>")

@bot.message_handler(commands=["wiki"])
def command_wiki(m):
    if m.text == "/wiki":
        bot.reply_to(m, "<b>Wrong command❗</b>\n[<code>/wiki your_text</code>]")
    else:
        text = m.text.replace("/wiki ", "")
        wait = bot.reply_to(m, "Please wait....⏳")
        API = f"https://api.zahwazein.xyz/information/wikipedia?query={text}&apikey={ZENZ_API}"
        wiki = requests.get(API).json()
        bot.delete_message(chat_id=wait.chat.id, message_id=wait.message_id)
        if wiki["status"] == "OK":
            result = wiki.get("result")
            text = "<b>🗞️ Tɪᴛʟᴇ : " +result["judul"]+ "</b>"
            text += "\n\n📖 " +result["isi"]
            if len(text) > 4095:
                for x in range(0, len(text), 4095):
                    bot.send_message(m.chat.id, text[x:x+4095])
            else:
                bot.reply_to(m, text)
        else:
            bot.reply_to(m, "<b>Can't connect API right now❗</b>")

@bot.message_handler(commands=["yt"])
def command_yt(m):
    if m.text == "/yt":
        bot.reply_to(m, "<b>Wrong command❗</b>\n[<code>/yt your_link</code>]")
    elif "https://youtu.be/" in m.text:
        global link
        link = m.text.replace("/yt ", "")
        wait = bot.reply_to(m, "Please wait....⏳")
        yt = YouTube(link)
        text = "<b>📽️ Tɪᴛʟᴇ :</b> " +str(yt.title)
        text += "\n<b>👀 Vɪᴇᴡꜱ :</b> " +str(yt.views)
        text += "\n<b>⚜️ Aᴜᴛʜᴏʀ :</b> " +str(yt.author)
        text += "\n<b>Dᴜʀᴀᴛɪᴏɴ :</b> " +str(yt.length)+ "MB"
        text += "\n<b>📅 Pᴜʙʟɪꜱʜ Dᴀᴛᴇ :</b> " +str(yt.publish_date)
        text += "\n<b>🌟 Rᴀᴛɪɴɢꜱ :</b> " +str(yt.rating)
        bot.delete_message(chat_id=wait.chat.id, message_id=wait.message_id)
        bot.send_photo(m.chat.id, str(yt.thumbnail_url), caption=text)

@bot.message_handler(content_types=["text"])
def reply(m):
    if m.text == "Joined ✅":
        bot.send_message(m.chat.id, "<b>Thank You 🌝❤️</b>", reply_markup=hideboard)
        command_help(m)
    if AUTO_REPLY == "True":
        if m.text.startswith("/"):
            pass
        else:
            bot.reply_to(m, openai.Completion.create(engine="text-davinci-003", prompt=m.text, max_tokens=1024, n=1, stop=None, temperature=0.5).choices[0].text)
    elif AUTO_REPLY == "False":
        pass
    else:
        pass

@bot.message_handler(content_types=["document", "photo", "audio", "video", "sticker", "video_note", "voice", "contact", "location"])
def send_id(m):
    bot.reply_to(m, "<b>Message ID</b> ➤ <code>" +str(m.message_id)+ "</code>")

def wait(call):
    wait = bot.send_message(call.message.chat.id, "Generating your logo....⏳")
    bot.send_chat_action(call.message.chat.id, 'upload_photo')
    bot.delete_message(call.message.chat.id, wait.message_id)

@bot.callback_query_handler(func=lambda call: True)
def callback_data(call):
    if call.data == "line":
        bot.answer_callback_query(call.id, random.choice(heart_emoji))
    elif call.data == "close_help":
        bot.delete_message(call.message.chat.id, close_help.message_id)
    elif call.data == "all_menu":
        text = "<b>👥 📜𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 ALL MENU📜</b>\n"
        Command_Emojys = ["🔥", "💞", "🔰", "💠", "♦️"]
        Desc_Emojys = ["📖", "📋", "🗒️", "📝", "📃"]
        Usage_Emojys = ["🏷️", "🔖", "✏️", "🖊️", "🔑"]
        cemojy = random.choice(Command_Emojys)
        demojy = random.choice(Desc_Emojys)
        uemojy = random.choice(Usage_Emojys)
        for key in ALL_MENU:
            text += "\n" +cemojy+ " <b>Cᴏᴍᴍᴀɴᴅ :</b> " +key
            text += "\n" +demojy+ " <b>Dᴇꜱᴄʀɪᴘᴛɪᴏɴ :</b> <i>" +ALL_MENU[key][0]+ "</i>"
            text += "\n" +uemojy+ " <b>Usage :</b> <code>" +ALL_MENU[key][1]+ "</code>\n"
        bot.edit_message_text(call.message.chat.id, text, help.message_id)
    elif call.data == "main_menu":
        text = "<b>👥 📜𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 MAIN MENU📜</b>\n"
        Command_Emojys = ["🔥", "💞", "🔰", "💠", "♦️"]
        Desc_Emojys = ["📖", "📋", "🗒️", "📝", "📃"]
        Usage_Emojys = ["🏷️", "🔖", "✏️", "🖊️", "🔑"]
        cemojy = random.choice(Command_Emojys)
        demojy = random.choice(Desc_Emojys)
        uemojy = random.choice(Usage_Emojys)
        for key in MAIN_MENU:
            text += "\n" +cemojy+ " <b>Cᴏᴍᴍᴀɴᴅ :</b> " +key
            text += "\n" +demojy+ " <b>Dᴇꜱᴄʀɪᴘᴛɪᴏɴ :</b> <i>" +MAIN_MENU[key][0]+ "</i>"
            text += "\n" +uemojy+ " <b>Usage :</b> <code>" +MAIN_MENU[key][1]+ "</code>\n"
        bot.edit_message_text(call.message.chat.id, text, help.message_id)
    elif call.data == "all menu":
        text = "<b>👥 📜𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 ALL MENU📜</b>\n"
        Command_Emojys = ["🔥", "💞", "🔰", "💠", "♦️"]
        Desc_Emojys = ["📖", "📋", "🗒️", "📝", "📃"]
        Usage_Emojys = ["🏷️", "🔖", "✏️", "🖊️", "🔑"]
        cemojy = random.choice(Command_Emojys)
        demojy = random.choice(Desc_Emojys)
        uemojy = random.choice(Usage_Emojys)
        for key in ALL_MENU:
            text += "\n" +cemojy+ " <b>Cᴏᴍᴍᴀɴᴅ :</b> " +key
            text += "\n" +demojy+ " <b>Dᴇꜱᴄʀɪᴘᴛɪᴏɴ :</b> <i>" +ALL_MENU[key][0]+ "</i>"
            text += "\n" +uemojy+ " <b>Usage :</b> <code>" +ALL_MENU[key][1]+ "</code>\n"
        bot.edit_message_text(call.message.chat.id, text, help.message_id)
    elif call.data == "all menu":
        text = "<b>👥 📜𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 ALL MENU📜</b>\n"
        Command_Emojys = ["🔥", "💞", "🔰", "💠", "♦️"]
        Desc_Emojys = ["📖", "📋", "🗒️", "📝", "📃"]
        Usage_Emojys = ["🏷️", "🔖", "✏️", "🖊️", "🔑"]
        cemojy = random.choice(Command_Emojys)
        demojy = random.choice(Desc_Emojys)
        uemojy = random.choice(Usage_Emojys)
        for key in ALL_MENU:
            text += "\n" +cemojy+ " <b>Cᴏᴍᴍᴀɴᴅ :</b> " +key
            text += "\n" +demojy+ " <b>Dᴇꜱᴄʀɪᴘᴛɪᴏɴ :</b> <i>" +ALL_MENU[key][0]+ "</i>"
            text += "\n" +uemojy+ " <b>Usage :</b> <code>" +ALL_MENU[key][1]+ "</code>\n"
        bot.edit_message_text(call.message.chat.id, text, help.message_id)
    elif call.data == "all menu":
        text = "<b>👥 📜𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 ALL MENU📜</b>\n"
        Command_Emojys = ["🔥", "💞", "🔰", "💠", "♦️"]
        Desc_Emojys = ["📖", "📋", "🗒️", "📝", "📃"]
        Usage_Emojys = ["🏷️", "🔖", "✏️", "🖊️", "🔑"]
        cemojy = random.choice(Command_Emojys)
        demojy = random.choice(Desc_Emojys)
        uemojy = random.choice(Usage_Emojys)
        for key in ALL_MENU:
            text += "\n" +cemojy+ " <b>Cᴏᴍᴍᴀɴᴅ :</b> " +key
            text += "\n" +demojy+ " <b>Dᴇꜱᴄʀɪᴘᴛɪᴏɴ :</b> <i>" +ALL_MENU[key][0]+ "</i>"
            text += "\n" +uemojy+ " <b>Usage :</b> <code>" +ALL_MENU[key][1]+ "</code>\n"
        bot.edit_message_text(call.message.chat.id, text, help.message_id)
    elif call.data == "all menu":
        text = "<b>👥 📜𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 ALL MENU📜</b>\n"
        Command_Emojys = ["🔥", "💞", "🔰", "💠", "♦️"]
        Desc_Emojys = ["📖", "📋", "🗒️", "📝", "📃"]
        Usage_Emojys = ["🏷️", "🔖", "✏️", "🖊️", "🔑"]
        cemojy = random.choice(Command_Emojys)
        demojy = random.choice(Desc_Emojys)
        uemojy = random.choice(Usage_Emojys)
        for key in ALL_MENU:
            text += "\n" +cemojy+ " <b>Cᴏᴍᴍᴀɴᴅ :</b> " +key
            text += "\n" +demojy+ " <b>Dᴇꜱᴄʀɪᴘᴛɪᴏɴ :</b> <i>" +ALL_MENU[key][0]+ "</i>"
            text += "\n" +uemojy+ " <b>Usage :</b> <code>" +ALL_MENU[key][1]+ "</code>\n"
        bot.edit_message_text(call.message.chat.id, text, help.message_id)
    elif call.data == "all menu":
        text = "<b>👥 📜𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 ALL MENU📜</b>\n"
        Command_Emojys = ["🔥", "💞", "🔰", "💠", "♦️"]
        Desc_Emojys = ["📖", "📋", "🗒️", "📝", "📃"]
        Usage_Emojys = ["🏷️", "🔖", "✏️", "🖊️", "🔑"]
        cemojy = random.choice(Command_Emojys)
        demojy = random.choice(Desc_Emojys)
        uemojy = random.choice(Usage_Emojys)
        for key in ALL_MENU:
            text += "\n" +cemojy+ " <b>Cᴏᴍᴍᴀɴᴅ :</b> " +key
            text += "\n" +demojy+ " <b>Dᴇꜱᴄʀɪᴘᴛɪᴏɴ :</b> <i>" +ALL_MENU[key][0]+ "</i>"
            text += "\n" +uemojy+ " <b>Usage :</b> <code>" +ALL_MENU[key][1]+ "</code>\n"
        bot.edit_message_text(call.message.chat.id, text, help.message_id)
    elif call.data == "all menu":
        text = "<b>👥 📜𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 ALL MENU📜</b>\n"
        Command_Emojys = ["🔥", "💞", "🔰", "💠", "♦️"]
        Desc_Emojys = ["📖", "📋", "🗒️", "📝", "📃"]
        Usage_Emojys = ["🏷️", "🔖", "✏️", "🖊️", "🔑"]
        cemojy = random.choice(Command_Emojys)
        demojy = random.choice(Desc_Emojys)
        uemojy = random.choice(Usage_Emojys)
        for key in ALL_MENU:
            text += "\n" +cemojy+ " <b>Cᴏᴍᴍᴀɴᴅ :</b> " +key
            text += "\n" +demojy+ " <b>Dᴇꜱᴄʀɪᴘᴛɪᴏɴ :</b> <i>" +ALL_MENU[key][0]+ "</i>"
            text += "\n" +uemojy+ " <b>Usage :</b> <code>" +ALL_MENU[key][1]+ "</code>\n"
        bot.edit_message_text(call.message.chat.id, text, help.message_id)
    elif call.data == "all menu":
        text = "<b>👥 📜𝚮𝐘𝐃𝚪𝚫 𝚩𝚯𝚻 ALL MENU📜</b>\n"
        Command_Emojys = ["🔥", "💞", "🔰", "💠", "♦️"]
        Desc_Emojys = ["📖", "📋", "🗒️", "📝", "📃"]
        Usage_Emojys = ["🏷️", "🔖", "✏️", "🖊️", "🔑"]
        cemojy = random.choice(Command_Emojys)
        demojy = random.choice(Desc_Emojys)
        uemojy = random.choice(Usage_Emojys)
        for key in ALL_MENU:
            text += "\n" +cemojy+ " <b>Cᴏᴍᴍᴀɴᴅ :</b> " +key
            text += "\n" +demojy+ " <b>Dᴇꜱᴄʀɪᴘᴛɪᴏɴ :</b> <i>" +ALL_MENU[key][0]+ "</i>"
            text += "\n" +uemojy+ " <b>Usage :</b> <code>" +ALL_MENU[key][1]+ "</code>\n"
        bot.edit_message_text(call.message.chat.id, text, help.message_id)
    elif call.data == "info":
        bot.send_message(call.message.chat.id, INFO, disable_web_page_preview=True)
    elif call.data == "view_apod":
        API = "https://api.sdbots.tk/apod"
        apod = requests.get(API).json()
        text = str(apod['explanation'])
        if len(text) > 4095:
            for x in range(0, len(text), 4095):
                bot.send_message(call.message.chat.id, text[x:x+4095])
        else:
            bot.send_message(call.message.chat.id, str(apod['explanation']))
    #elif call.data == "info":
        #bot.edit_message_text(call.message.chat.id, INFO, help.message_id, disable_web_page_preview=True)
    elif call.data == "view_news":
        API = "https://api.sdbots.tk/hirunews"
        hirunews = requests.get(API).json()
        text = str(hirunews['description'])
        if len(text) > 4095:
            for x in range(0, len(text), 4095):
                bot.send_message(call.message.chat.id, text[x:x+4095])
        else:
            bot.send_message(call.message.chat.id, str(hirunews['description']))
    elif call.data == "American-Flag":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/americanflag?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Anime":
        wait(call)
        bot.send_photo(call.message.chat.id, anime_logo(logoA_text), caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Awan":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/awan?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Beach":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/beach?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Berry":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/berry?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Black-Pink":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/blackpink?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Blue-Circuit":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/bluecircuit?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Bohlam":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/bohlam?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Cake":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/cake?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Coklat":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/coklat?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Christmas":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/christmas?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Cracked-Stone":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/crackedstone?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Cross-Fire":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/crossfire?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Cute-Puppy":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/puppycute?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Drop-Water":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/dropwater?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Fiction":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/fiction?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Firework":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/firework?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Flash-Light":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/flashlight?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Flower":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/flower?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Foggy-Windows":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/foggywindows?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "FreeFire-Cover":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/ffcover?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Galaxy":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/galaxy?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Gaming":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/logogaming?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Girl":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/logogirl?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Glass":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/glass?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Glitch":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/impressiveglitch?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Glue":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/gluetext?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Gold":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/logogold?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Grafity":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/grafity?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Green-Horror":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/greenhorror?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Halloween":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/halloween?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Harry-Potter":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/harrypotter?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Kaligrafi":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/kaligrafi?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Logo":
        wait(call)
        bot.send_photo(call.message.chat.id, random.choice(f"https://api.zahwazein.xyz/ephoto/logo2?text={logoA_text}&apikey={ZENZ_API}", f"https://api.zahwazein.xyz/ephoto/logo3?text={logoA_text}&apikey={ZENZ_API}", f"https://api.zahwazein.xyz/ephoto/logo4?text={logoA_text}&apikey={ZENZ_API}"), caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Magma":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/magma?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Marmer":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/marmer?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Matrix":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/matrix?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Metallic":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/metallic?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Muslim-Semi":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/musimsemi?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Natural":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/natural?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Neon":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/neon?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Neon-Devil":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/neondevil?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Quotes":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/quotes?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Ruby":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/ruby?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Shadow":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/shadowtext?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Sketch":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/sketch?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Space":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/space?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Spider":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/spiderlogo?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Star":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/starlogo?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Star-Night":
        wait(call)
        bot.send_photo(call.message.chat.id, random.choice(f"https://api.zahwazein.xyz/ephoto/starnight?text={logoA_text}&apikey={ZENZ_API}", f"https://api.zahwazein.xyz/ephoto/starnight2?text={logoA_text}&apikey={ZENZ_API}"), caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Thunder":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/thunder?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Transformer":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/transformer?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Wallpaper":
        wait(call)
        bot.send_photo(call.message.chat.id, logohq(logoA_text), caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Write":
        wait(call)
        bot.send_photo(call.message.chat.id, write(logoA_text), caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Yasuo":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/yasuologo?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Certificate":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/certificate?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Instragram-Certificate":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/igcertificate?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Youtube-Certificate":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/ytcertificate?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Glitch1":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/glitch?text={logoB_text[0]}&text2={logoB_text[1]}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Marval":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/marvel?text={logoB_text[0]}&text2={logoB_text[1]}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Piring-Kaligrafi":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/piringkaligrafi?text={logoB_text[0]}&text2={logoB_text[1]}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Pornhub":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/pornhub?text={logoB_text[0]}&text2={logoB_text[1]}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Quotes1":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/quotesonline?text={logoB_text[0]}&text2={logoB_text[1]}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Sparkling":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/sparkling?text={logoB_text[0]}&text2={logoB_text[0]}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Typography":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/typography?text={logoB_text[0]}&text2={logoB_text[1]}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Wolf":
        wait(call)
        bot.send_photo(call.message.chat.id, random.choice([f"https://api.zahwazein.xyz/textpro/logowolf?text={logoB_text[0]}&text2={logoB_text[1]}&apikey={ZENZ_API}", f"https://api.zahwazein.xyz/textpro/logowolf2?text={logoB_text[0]}&text2={logoB_text[1]}&apikey={ZENZ_API}"]), caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Pro-Yector":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/proyektor?text={logoC_text[0]}&text2={logoC_text[1]}&text3={logoC_text[2]}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Valorant":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/ephoto/valorant?text={logoC_text[0]}&text2={logoC_text[1]}&text3={logoC_text[2]}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Christmas1":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/3dchristmas?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Deep-Sea":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/3ddeepsea?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Gradient":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/3dgradient?text={logoA_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Neon-Light":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/3dneonlight?text={logo3D_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Rainbow":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/3drainbow?text={logo3D_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Scifi":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/3dscifi?text={logo3D_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "Water-Pipe":
        wait(call)
        bot.send_photo(call.message.chat.id, f"https://api.zahwazein.xyz/textpro/3dwaterpipe?text={logo3D_text}&apikey={ZENZ_API}", caption=f"🖼️ Cᴀᴛᴇɢᴏʀʏ : {call.data}\n\n<a href='t.me/HydraBotSupport'>「© ᴘᴏᴡᴇʀᴇᴅ ʙʏ ʜʏᴅʀᴀ™」</a>")
    elif call.data == "morning":
        bot.answer_callback_query(call.id, random.choice(heart_emoji))
        bot.delete_message(call.message.chat.id, send_morning.message_id)
    elif call.data == "night":
        night_emoji = ["😴", "💤"]
        bot.answer_callback_query(call.id, random.choice(night_emoji))
        bot.delete_message(call.message.chat.id, send_night.message_id)


def morning():
    for i in users:
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        morning = types.InlineKeyboardButton(text="🌅 GOOD MORNING 🌅", callback_data="morning")
        send_morning = bot.send_photo(i, "", caption="")

def night():
    for i in users:
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        night = types.InlineKeyboardButton(text="🥱 GOOD NIGHT 🥱", callback_data="night")
        send_night = bot.send_photo(i, "", caption="")

schedule.every().day.at("06:00").do(morning)
schedule.every().day.at("22:00").do(night)

try:
    print ("\n\033[1;32mBot is alive\033[0m")
    bot.infinity_polling()
except Exception as e:
    print (e)

while True:
    schedule.run_pending()