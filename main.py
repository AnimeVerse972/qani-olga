import os
from aiogram import Bot, Dispatcher, types
from aiogram.executor import start_polling  # <-- executorni toza usulda import qilish
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keep_alive import keep_alive
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '7802093581:AAHdjDY2gWFpSjHrSyIOmQUJw1QX1BBb-H4'
CHANNELS = ['@AniVerseClip']
ADMINS = [6486825926, 7575041003]

bot = Bot(token=API_TOKEN, parse_mode="Markdown")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

keep_alive()

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    not_subscribed = []

    for channel in CHANNELS:
        try:
            chat_member = await bot.get_chat_member(channel, user_id)
            if chat_member.status not in ['member', 'administrator', 'creator']:
                not_subscribed.append(channel)
        except:
            not_subscribed.append(channel)

    if not_subscribed:
        keyboard = InlineKeyboardMarkup(row_width=1)
        for ch in not_subscribed:
            keyboard.add(InlineKeyboardButton(f"🔔 {ch}", url=f"https://t.me/{ch.strip('@')}"))
        await message.reply("⛔ Iltimos, quyidagi kanallarga obuna bo‘ling:", reply_markup=keyboard)
        return

    text = "✅ Assalomu alaykum! Anime kodi yuboring (masalan: 1, 2, 3, ...)"

    buttons = [
        [KeyboardButton("📢 Reklama"), KeyboardButton("💼 Homiylik")]
    ]
    if user_id in ADMINS:
        buttons.append([KeyboardButton("🛠 Admin panel")])

    reply_markup = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        one_time_keyboard=True
    )

    await message.reply(text, reply_markup=reply_markup)


@dp.message_handler(lambda message: message.text == "📢 Reklama")
async def reklama_handler(message: types.Message):
    await message.reply("Reklama uchun: @DiyorbekPTMA")

@dp.message_handler(lambda message: message.text == "💼 Homiylik")
async def homiylik_handler(message: types.Message):
    await message.reply("Homiylik uchun karta: **8800904257677885**")

@dp.message_handler(lambda message: message.text == "🛠 Admin panel")
async def admin_panel_handler(message: types.Message):
    if message.from_user.id in ADMINS:
        await message.reply("👮‍♂️ Admin paneliga xush kelibsiz!\nHozircha hech qanday amallar yo‘q.")
    else:
        await message.reply("⛔ Siz admin emassiz!")


@dp.message_handler()
async def anime_code_handler(message: types.Message):
    code = message.text.strip()

    anime_posts = {
        "1": {"channel": "@AniVerseClip", "message_id": 10},
        "2": {"channel": "@AniVerseClip", "message_id": 23},
        "3": {"channel": "@AniVerseClip", "message_id": 35},
        "4": {"channel": "@AniVerseClip", "message_id": 49},
        "5": {"channel": "@AniVerseClip", "message_id": 76},
        "6": {"channel": "@AniVerseClip", "message_id": 104},
        "7": {"channel": "@AniVerseClip", "message_id": 851},
        "8": {"channel": "@AniVerseClip", "message_id": 127},
        "9": {"channel": "@AniVerseClip", "message_id": 131},
        "10": {"channel": "@AniVerseClip", "message_id": 135},
        "11": {"channel": "@AniVerseClip", "message_id": 148},
        "12": {"channel": "@AniVerseClip", "message_id": 200},
        "13": {"channel": "@AniVerseClip", "message_id": 216},
        "14": {"channel": "@AniVerseClip", "message_id": 222},
        "15": {"channel": "@AniVerseClip", "message_id": 235},
        "16": {"channel": "@AniVerseClip", "message_id": 260},
        "17": {"channel": "@AniVerseClip", "message_id": 360},
        "18": {"channel": "@AniVerseClip", "message_id": 379},
        "19": {"channel": "@AniVerseClip", "message_id": 392},
        "20": {"channel": "@AniVerseClip", "message_id": 405},
        "21": {"channel": "@AniVerseClip", "message_id": 430},
        "22": {"channel": "@AniVerseClip", "message_id": 309},
        "23": {"channel": "@AniVerseClip", "message_id": 343},
        "24": {"channel": "@AniVerseClip", "message_id": 501},
        "25": {"channel": "@AniVerseClip", "message_id": 514},
        "26": {"channel": "@AniVerseClip", "message_id": 462},
        "27": {"channel": "@AniVerseClip", "message_id": 527},
        "28": {"channel": "@AniVerseClip", "message_id": 542},
        "29": {"channel": "@AniVerseClip", "message_id": 555},
        "30": {"channel": "@AniVerseClip", "message_id": 569},
        "31": {"channel": "@AniVerseClip", "message_id": 586},
        "32": {"channel": "@AniVerseClip", "message_id": 624},
        "33": {"channel": "@AniVerseClip", "message_id": 638},
        "34": {"channel": "@AniVerseClip", "message_id": 665},
        "35": {"channel": "@AniVerseClip", "message_id": 696},
        "36": {"channel": "@AniVerseClip", "message_id": 744},
        "37": {"channel": "@AniVerseClip", "message_id": 776},
        "38": {"channel": "@AniVerseClip", "message_id": 789},
        "39": {"channel": "@AniVerseClip", "message_id": 802},
        "40": {"channel": "@AniVerseClip", "message_id": 815},
        "41": {"channel": "@AniVerseClip", "message_id": 835},
        "42": {"channel": "@AniVerseClip", "message_id": 864},
        "43": {"channel": "@AniVerseClip", "message_id": 918},
        "44": {"channel": "@AniVerseClip", "message_id": 931},
        "45": {"channel": "@AniVerseClip", "message_id": 946}
    }

    if code in anime_posts:
        post = anime_posts[code]
        try:
            # Postni nusxalab yuborish
            sent_msg = await bot.copy_message(
                chat_id=message.chat.id,
                from_chat_id=post['channel'],
                message_id=post['message_id']
            )

            # Tugma yaratish
            msg_link = f"https://t.me/{post['channel'].strip('@')}/{post['message_id']}"
            keyboard = InlineKeyboardMarkup().add(
                InlineKeyboardButton("⬇️ Yuklab olish", url=msg_link)
            )

            # Tugmani nusxa olingan postga biriktirish
            await bot.edit_message_reply_markup(
                chat_id=message.chat.id,
                message_id=sent_msg.message_id,
                reply_markup=keyboard
            )

        except Exception as e:
            print(f"Xatolik: {e}")
            await message.reply("❌ Xatolik yuz berdi. Bot kanalga admin qilinganligini tekshiring.")
    else:
        await message.reply("❌ Bunday kod topilmadi. Iltimos, to‘g‘ri anime kodini yuboring.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
