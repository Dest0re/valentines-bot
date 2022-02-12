from peewee import PrimaryKeyField, ForeignKeyField, BooleanField, TextField, DateTimeField

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
    created_at = DateTimeField(column_name='creation_datetime')

    class Meta:
        table_name = 'ValentineCard'

    @classmethod
    def get_last_presenter_card_or_none(cls, presenter: Presenter):
        card = (
            cls
            .select()
            .where(cls.presenter == presenter, cls.in_process)
            .order_by(cls.id.desc())
            .get_or_none()
        )

        return card

