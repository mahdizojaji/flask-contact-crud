import os
from config import BASE_DIR
from peewee import SqliteDatabase, Model, CompositeKey
from peewee import IntegerField, CharField

db = SqliteDatabase(os.path.join(BASE_DIR, 'flask-db.sqlite3'), pragmas={
    'journal_mode': 'wal',
    'cache_size': 10000,
    'foreign_keys': 1,
    'ignore_check_constraints': 0,
    'synchronous': 0
})


class BaseModel(Model):
    class Meta:
        database = db


class Contact(BaseModel):
    _id = IntegerField(unique=True)
    name = CharField()
    phone = CharField()

    class Meta:
        primary_key = CompositeKey('_id')
