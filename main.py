import telebot
from settings import bot_token
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import db_functions
from re import search
import time

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Привет, теперь ты в базе")
    db_functions.save_user(message.chat.id)


@bot.message_handler(func=lambda message: message.text.startswith("задача"))
def get_task(message):
    bot.send_message(message.chat.id, "Вас понял! Таск добавлен!")
    # print(message.chat.id)
    list_of_users = db_functions.create_list_from_users_db()
    for i in list_of_users:
        msg = bot.send_message(i, message.text + " " + str(message.id), reply_markup=gen_markup())
        msg_id = msg.message_id




def get_last_message_id(message):
    last_message_id = message.id


def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Сделано", callback_data="cb_done"),
                               InlineKeyboardButton("Удалить", callback_data="cb_del"))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_done":
        bot.answer_callback_query(call.id, "Таск выполнен")
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id, text=call.message.text +" ВЫПОЛНЕНО",
                              parse_mode='Markdown')
    elif call.data == "cb_del":
        bot.answer_callback_query(call.id, "Таск удален")


@bot.message_handler(func=lambda message: message.text == "таски")
def send_message(message):
    bot.send_message(message.chat.id, "Вот актуальный список тасков:")









bot.polling()