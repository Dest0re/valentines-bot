from peewee import PrimaryKeyField, ForeignKeyField

from .basemodel import BaseModel
from .user import User


class Presenter(BaseModel):
    id = PrimaryKeyField(column_name='presenter_id')
    user = ForeignKeyField(User, column_name='user_id')

    class Meta:
        table_name = 'Presenter'
