from peewee import PrimaryKeyField, ForeignKeyField

from .basemodel import BaseModel
from .user import User


class Receiver(BaseModel):
    id = PrimaryKeyField(column_name='receiver_id')
    user = ForeignKeyField(User, column_name='user_id')

    class Meta:
        table_name = 'Receiver'
