import discord

from utils.embed import DebugText
from .abstractbasehandler import StopHandleException
from .basehandler import BaseHandler
from model import ValentineCard, User, Presenter


class MarkCardAsSpecialHandler(BaseHandler):
    async def _handle(self, ctx: discord.ApplicationContext):
        user = User.get_or_none(discord_user_id=ctx.author.id)

        if not user:
            raise StopHandleException(str(__class__))

        presenter = Presenter.get_or_create(user=user)[0]

        card = ValentineCard.get_last_presenter_card_or_none(presenter)

        if not card:
            raise StopHandleException(str(__class__))

        card.is_special = True

        card.save()
