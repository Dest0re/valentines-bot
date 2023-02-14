from peewee import PrimaryKeyField, ForeignKeyField

from .basemodel import BaseModel
from .user import User


class Presenter(BaseModel):
    id = PrimaryKeyField(column_name='presenter_id')
    user = ForeignKeyField(User, column_name='user_id')

    class Meta:
        table_name = 'presenters'

    @classmethod
    def from_discord_id(cls, discord_id):
        user = User.from_discord_id(discord_id)

        return cls.get_or_create(user=user)[0]
