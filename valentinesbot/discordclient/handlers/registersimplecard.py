import discord

from utils.embed import DebugText, ErrorText
from .basehandler import BaseHandler

from model import ValentineCard, Presenter, User


class RegisterSimpleCardHandler(BaseHandler):
    async def _handle(self, ctx: discord.ApplicationContext):
        user = User.get_or_none(discord_user_id=ctx.author.id)

        if not user:
            await ctx.respond(embed=ErrorText('Что-то пошло не так'))

        presenter = Presenter.get_or_create(user=user)[0]

        ValentineCard.create(presenter=presenter, in_process=True)
