from peewee import *

sqlite_db = SqliteDatabase('task tracker.db', pragmas={'journal_mode': 'wal'})

class BaseModel(Model):
    """A base model that will use our Sqlite database."""
    class Meta:
        database = sqlite_db


class TaskTracker(BaseModel):
    id = IntegerField(primary_key=True)
    text = TextField()
    status = TextField()
    date = TextField()

class Messages(BaseModel):
    id = IntegerField(primary_key=True)
    task_id = TextField()
    chat_id = TextField()
    message_id = TextField()

class User(BaseModel):
    id = IntegerField(primary_key=True)
    chat_id = IntegerField()