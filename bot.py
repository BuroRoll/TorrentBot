import telebot
from par import Parser


class Bot(object):
    def __init__(self, token):
        self.bot = telebot.TeleBot(token, parse_mode=None)
        self.links = []
        self.parser = Parser()

        @self.bot.callback_query_handler(func=lambda call: True)
        def download_torrent(call):
            self.parser.download_torrent(self.links[int(call.data)])

        @self.bot.message_handler()
        def send_torrents(message):
            data = self.parser.get_torrents(message.text)
            self.links.clear()
            for key, value in data.items():
                self.links.append(value)
            names = list(data)
            for i in range(len(data)):
                markup = telebot.types.InlineKeyboardMarkup()
                num = str(i)
                button = telebot.types.InlineKeyboardButton(text='Скачать', callback_data=num)
                markup.add(button)
                self.bot.send_message(message.chat.id, names[i], reply_markup=markup)

        self.bot.polling()
