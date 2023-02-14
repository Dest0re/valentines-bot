import discord

from utils.embed import DebugText, EmbedText
from .basehandler import BaseHandler
from model import User, Presenter, ValentineCard
from utils.strings import text_strings as ts


class CheckIfCanGiftSpecialCardHandler(BaseHandler):
    async def _handle(self, ctx: discord.ApplicationContext):
        presenter = Presenter.from_discord_id(ctx.author.id)

        special_cards = (
            ValentineCard
            .select()
            .where(
                ValentineCard.is_special == True,
                ValentineCard.do_present == True,
                ValentineCard.in_process == False,
                ValentineCard.presenter == presenter
            )
            .execute()
        )

        print(1)
        if len(tuple(special_cards)) < 1:
            await ctx.respond(embed=EmbedText(ts.can_give_special_card))
