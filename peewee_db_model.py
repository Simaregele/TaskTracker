from peewee import *

sqlite_db = SqliteDatabase('task tracker.db', pragmas={'journal_mode': 'wal'})

class BaseModel(Model):
    """A base model that will use our Sqlite database."""
    class Meta:
        database = sqlite_db


class taskTracker(BaseModel):
    id = IntegerField(primary_key=True)
    text = TextField()
    status = TextField()
    users_id = TextField()
    messages_id = TextField()

class User(BaseModel):
    id = IntegerField(primary_key=True)
    chat_id = IntegerField()