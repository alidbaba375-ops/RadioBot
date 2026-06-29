from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

TOKEN = "8734797446:AAEbyUi4rTM2D0bB8eD6zwusBhkxG9kq5aA"

تعريف المحطات مع صور صغيرة

stations = {
"quran": [
{"name": "مشاري العفاسي", "url": "https://qurango.net/radio/mishary_alafasi", "photo": "https://i.imgur.com/9y1U6bR.png"},
{"name": "تراتيل قصيرة متميزة", "url": "https://qurango.net/radio/tarateel", "photo": "https://i.imgur.com/3H5L7Gk.png"},
{"name": "القارئ محمد أيوب", "url": "https://qurango.net/radio/mohammed_ayyub", "photo": "https://i.imgur.com/jF8uGZa.png"},
{"name": "مختصر التفسير", "url": "https://qurango.net/radio/mukhtasartafsir", "photo": "https://i.imgur.com/d8nD2bX.png"},
{"name": "ماهر المعيقلي", "url": "https://backup.qurango.net/radio/maher", "photo": "https://i.imgur.com/KrF2M6y.png"},
],
"mix": [
{"name": "87.8 Mix FM", "url": "https://stream-29.zeno.fm/na3vpvn10qruv", "photo": "https://i.imgur.com/O6sYtFq.png"},
{"name": "90s FM", "url": "http://eu1.fastcast4u.com/proxy/prontofm", "photo": "https://i.imgur.com/BlY8N6u.png"},
{"name": "Amr Diab Radio", "url": "https://stream-40.zeno.fm/xa4yhh4k838uv?zs=gojgaFRaRrK1wgGIwdv6xA", "photo": "https://i.imgur.com/Hf1f4Wv.png"},
],
"arab": [
{"name": "Arab Mix 256", "url": "https://stream.zeno.fm/wvqgc9kb1d0uv", "photo": "https://i.imgur.com/Yz9zJ3R.png"},
{"name": "Arab Mix Drama", "url": "https://stream.zeno.fm/egynebf171zuv.acc", "photo": "https://i.imgur.com/2c9mz3P.png"},
{"name": "Arab Mix FM", "url": "https://stream.zeno.fm/na3vpvn10qruv", "photo": "https://i.imgur.com/BfT0r2K.png"},
]
}

رسالة البداية

def start(update, context):
buttons = [
[InlineKeyboardButton("📿 قرآن", callback_data="quran")],
[InlineKeyboardButton("🎶 Mix", callback_data="mix")],
[InlineKeyboardButton("🌍 Arab", callback_data="arab")]
]
update.message.reply_text("اختر نوع الإذاعة:", reply_markup=InlineKeyboardMarkup(buttons))

عرض المحطات مع الصور

def show_stations(update, context):
query = update.callback_query
query.answer()
section = stations.get(query.data, [])

for s in section:  
    buttons = [[InlineKeyboardButton("▶️ استمع", url=s["url"])]]  
    context.bot.send_photo(  
        chat_id=query.message.chat.id,  
        photo=s["photo"],  
        caption=s["name"],  
        reply_markup=InlineKeyboardMarkup(buttons)  
    )

إنشاء التطبيق

updater = Updater(TOKEN)
dispatcher = updater.dispatcher

إضافة الهاندلرز

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CallbackQueryHandler(show_stations))

print("Bot is running...")
updater.start_polling()
updater.idle()
