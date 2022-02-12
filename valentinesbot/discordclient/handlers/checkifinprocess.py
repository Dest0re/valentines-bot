import discord

from model import ValentineCard, Presenter, User
from utils.embed import DebugText, ErrorText
from .basehandler import BaseHandler
from .abstractbasehandler import StopHandleException


class CheckIfInProcessHandler(BaseHandler):
    async def _handle(self, ctx: discord.ApplicationContext):
        user = User.get_or_none(discord_user_id=ctx.author.id)

        if not user:
            raise StopHandleException(str(__class__))

        presenter = Presenter.get_or_create(user=user)[0]

        card = ValentineCard.get_last_presenter_card_or_none(presenter)

        if card:
            await ctx.respond(embed=ErrorText('Сперва закончите с предыдущей валентинкой!'))
            raise StopHandleException(str(__class__))

    async def _exc(self, ctx: discord.ApplicationContext):
        pass
