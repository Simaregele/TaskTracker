import telebot
from settings import bot_token
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import db_functions
import time

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Привет, теперь ты в базе")
    db_functions.save_user(message.chat.id)


@bot.message_handler(func=lambda message: message.text.startswith('задача'))
def get_task(message):
    task_id = db_functions.save_task_to_DB_and_return_its_id(text=message.text, status="open", date=message.date)
    bot.send_message(message.chat.id, "Вас понял! Таск добавлен!")
    list_of_users = db_functions.create_list_from_users_db()
    for i in list_of_users:
        msg = bot.send_message(i, message.text, reply_markup=gen_markup())
        time.sleep(0.05)
        db_functions.create_ids_records_for_task(task_id=task_id, chat_id=msg.chat.id, message_id=msg.message_id)

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Сделано", callback_data="cb_done"),
                               InlineKeyboardButton("Удалить", callback_data="cb_del"))
    return markup

# тут у нас функции которые изменяют существующий таск
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_done":
        bot.answer_callback_query(call.id, "Таск выполнен")
        edit_task(chat_id=call.message.chat.id, message_id=call.message.message_id,
                  status="done", text=call.message.text)
    elif call.data == "cb_del":
        bot.answer_callback_query(call.id, "Таск удален")


def edit_task(chat_id, message_id, status, text):
    task_id = db_functions.return_task_id(chat_id=chat_id, message_id=message_id)
    db_functions.edit_task_status(status=status, task_id=task_id)
    mess_and_chats = db_functions.return_messages_and_chats_ids(task_id=task_id)
    for i in mess_and_chats:
        bot.edit_message_text(chat_id=i.chat_id, message_id=i.message_id, text=text + " Таск выполнен",
                              parse_mode='Markdown')


@bot.message_handler(func=lambda message: message.text == "таски")
def send_message(message):
    bot.send_message(message.chat.id, "Вот актуальный список тасков:")


bot.polling()