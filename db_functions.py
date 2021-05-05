from peewee import *
from peewee_db_model import taskTracker, User
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
def save_task(message, chat_id, message_id):
    new_task = taskTracker()

def create_list_to_save_in_tasks(list_of_users):
    return json.dumps(list_of_users)

def get_list_from_tasks():
    pass

def create_task_DB(text, ):
    new_tsk = taskTracker(text=text, status="open")
    new_tsk.save()

def create_text_for_tsk():
    pass

def create_status_for_tsk():
    pass

def change_status_for_tsk():
    pass

def change_text_for_tsk():
    pass