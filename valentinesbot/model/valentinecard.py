from peewee import PrimaryKeyField, ForeignKeyField, BooleanField, TextField

from .basemodel import BaseModel
from .presenter import Presenter
from .receiver import Receiver


class ValentineCard(BaseModel):
    id = PrimaryKeyField(column_name='valentine_card_id')
    presenter = ForeignKeyField(Presenter, column_name='presenter_id')
    is_anonymous = BooleanField(column_name='is_anonymous')
    content = TextField(column_name='content')
    is_special = BooleanField(column_name='is_special')
    receiver = ForeignKeyField(Receiver, column_name='receiver_id')
    in_process = BooleanField(column_name='is_in_process')
    do_present = BooleanField(column_name='do_present')

    class Meta:
        table_name = 'ValentineCard'
