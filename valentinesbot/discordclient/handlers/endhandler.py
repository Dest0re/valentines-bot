import discord

from model import ValentineCard, Presenter, User
from utils.embed import DebugText
from .basehandler import BaseHandler


class EndHandler(BaseHandler):
    async def _handle(self, ctx: discord.ApplicationContext):
        user = User.get_or_none(discord_user_id=ctx.author.id)

        if user:
            presenter = Presenter.get_or_create(user=user)[0]

            card = ValentineCard.get_last_presenter_card_or_none(presenter)

            if card:
                card.in_process = False
                card.save()
