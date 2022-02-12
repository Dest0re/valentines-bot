import discord
from discord.commands import slash_command
from discord.ext import commands

from .basecog import BaseCog
from discordclient.handlers import *


async def _handle_command(ctx: discord.ApplicationContext, is_special: bool):
    handler = RegisterSimpleUserHandler()
    next_handler = handler.set_next(CheckIfInProcessHandler())

    if not is_special:
        next_handler = next_handler.set_next(CheckIfCanGiftSpecialCardHandler())

    next_handler = next_handler.set_next(RegisterSimpleCardHandler())

    if is_special:
        next_handler = next_handler\
            .set_next(CheckIfCannotGiftSpecialCardHandler())\
            .set_next(MarkCardAsSpecialHandler())

    (
        next_handler
        .set_next(SelectReceiverHandler())
        .set_next(GetCardContentHandler())
        .set_next(AskForAnonymityHandler())
        .set_next(SendPreviewHandler())
        .set_next(SuccessHandler())
        .set_next(EndHandler())
    )

    await handler.do_handle(ctx)


class GiftingCog(BaseCog):
    @slash_command(name='gift', description='Подарить валентинку')
    @commands.dm_only()
    async def _gift(self, ctx: discord.ApplicationContext):
        await _handle_command(ctx, False)

    @slash_command(name='gift-special', description='Подарить ОСОБУЮ валентинку!')
    @commands.dm_only()
    async def _gift_special(self, ctx: discord.ApplicationContext):
        await _handle_command(ctx, True)
