import telebot
import par

bot = telebot.TeleBot('TOKEN', parse_mode=None)
links = []


@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    par.download_torrent(links[int(call.data)])


@bot.message_handler()
def send_welcome(message):
    data = par.get_torrents(message.text)
    links.clear()
    for key, value in data.items():
        links.append(value)
    names = list(data)
    for i in range(len(data)):
        markup = telebot.types.InlineKeyboardMarkup()
        num = str(i)
        button = telebot.types.InlineKeyboardButton(text='Скачать', callback_data=num)
        markup.add(button)
        bot.send_message(message.chat.id, names[i], reply_markup=markup)


bot.polling()
