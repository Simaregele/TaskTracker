from peewee import *
from peewee_db_model import TaskTracker, User, Messages
import json

# users db functions
def save_user(chat_id):
    new_user = User(chat_id=chat_id)
    new_user.save()

def create_list_from_users_db():
    list_of_users = User.select()
    list_from_users_db = []
    for i in list_of_users:
        list_from_users_db.append(i.chat_id)
    # print(list_from_users_db)
    return list_from_users_db

# tasks db functions
def save_task_to_DB_and_return_its_id(text, status, date):
    # Сохраняет в базу и возвращает id сохраненной записис
    new_tsk = TaskTracker(text=text, status=status, date=date)
    new_tsk.save()
    return new_tsk.id

def create_ids_records_for_task(task_id, chat_id, message_id):
    Messages(task_id=task_id, chat_id=chat_id, message_id=message_id).save()

def return_messages_and_chats_ids(task_id):
    # возвращает все записи с данными по id
    return Messages.select().where(Messages.task_id==task_id)

def return_task_id(chat_id, message_id):
    ids = Messages.select().where(Messages.chat_id==chat_id, Messages.message_id==message_id)
    for i in ids:
        return i.task_id

def edit_task_status(task_id, status):
    TaskTracker.update(status=status).where(TaskTracker.id==task_id).execute()

def get_list_from_tasks():
    pass

def create_text_for_tsk():
    pass

def create_status_for_tsk():
    pass

def change_status_for_tsk():
    pass

def change_text_for_tsk():
    pass