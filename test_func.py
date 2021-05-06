from peewee import *
from peewee_db_model import TaskTracker, User, Messages
import json
import db_functions


some_var = Messages.select().where(Messages.chat_id=="185604193", Messages.message_id=="123")
for i in some_var:
    print(i.task_id)



