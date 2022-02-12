import asyncio

import discord

from utils.embed import DebugText, ErrorText
from .abstractbasehandler import StopHandleException
from .basehandler import BaseHandler
from model import ValentineCard, Presenter, User
from utils.strings import text_strings as ts


class GetCardContentHandler(BaseHandler):
    async def _handle(self, ctx: discord.ApplicationContext):
        user = User.get_or_none(discord_user_id=ctx.author.id)

        if not user:
            raise StopHandleException(str(__class__))

        presenter = Presenter.get_or_create(user=user)[0]

        card = ValentineCard.get_last_presenter_card_or_none(presenter)

        if not card:
            raise StopHandleException(str(__class__))

        await ctx.respond(ts.waiting_for_content)

        try:
            message = await ctx.bot.wait_for(
                'message',
                check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel_id,
                timeout=300
            )
        except asyncio.TimeoutError:
            await ctx.respond(embed=ErrorText(ts.timeout_error))

            raise StopHandleException(str(__class__))

        card.content = message.content[:300]
        card.save()
