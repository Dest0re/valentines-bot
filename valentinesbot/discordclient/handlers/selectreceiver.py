import asyncio

import discord

from utils.embed import DebugText, EmbedText, ErrorText, WarningText
from .abstractbasehandler import StopHandleException
from .basehandler import BaseHandler
from utils.strings import text_strings as ts
from model import User, Receiver, Presenter, ValentineCard


class SelectReceiverHandler(BaseHandler):
    async def _handle(self, ctx: discord.ApplicationContext):
        await ctx.respond('ieijfiejfij')
        await ctx.respond(embed=EmbedText(ts.select_receiver_message))

        for _ in range(3):
            try:
                message = await ctx.bot.wait_for(
                    'message',
                    check=lambda m: m.author == ctx.author and m.channel.id == ctx.channel_id,
                    timeout=300
                )
            except asyncio.TimeoutError:
                await ctx.respond(embed=WarningText(ts.timeout_error))
                continue

            if not message.content:
                await ctx.respond(embed=WarningText(ts.invalid_format))
                continue

            receiver_nickname = message.content
            cannot_give_twice = False

            for member in ctx.bot.get_all_members():
                if str(member) == receiver_nickname:
                    receiver = member

                    user = User.get_or_none(discord_user_id=ctx.author.id)

                    if not user:
                        raise StopHandleException(str(__class__))

                    presenter = Presenter.get_or_create(user=user)[0]

                    receiver_user = User.get_or_create(discord_user_id=receiver.id)[0]
                    receiver_model = Receiver.get_or_create(user=receiver_user)[0]

                    cards = (
                        ValentineCard
                        .select()
                        .where(
                            ValentineCard.presenter == presenter,
                            ValentineCard.receiver == receiver_model,
                            ValentineCard.in_process == False,
                            ValentineCard.do_present == True
                        )
                        .execute()
                    )

                    if len(cards) > 0:
                        cannot_give_twice = True
                        continue

                    break
            else:
                if cannot_give_twice:
                    await ctx.respond(embed=WarningText(ts.cannot_give_twice_error))
                else:
                    await ctx.respond(embed=WarningText(ts.member_does_not_exist))

                continue

            break
        else:
            await ctx.respond(embed=ErrorText(ts.select_receiver_error))

            raise StopHandleException(str(__class__))

        card = ValentineCard.get_last_presenter_card_or_none(presenter)

        if not card:
            raise StopHandleException(str(__class__))

        card.receiver = receiver_model
        card.save()
