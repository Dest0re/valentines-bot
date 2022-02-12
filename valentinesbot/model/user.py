from peewee import PrimaryKeyField, BigIntegerField

from .basemodel import BaseModel


class User(BaseModel):
    id = PrimaryKeyField(column_name='user_id')
    discord_user_id = BigIntegerField(column_name='discord_user_id')

    class Meta:
        table_name = 'User'

    @classmethod
    def from_discord_id(cls, discord_id):
        return cls.get(discord_user_id=discord_id)
