import discord

from utils.embed import DebugText, EmbedText
from .basehandler import BaseHandler
from model import User, Presenter, ValentineCard
from utils.strings import text_strings as ts


class CheckIfCanGiftSpecialCardHandler(BaseHandler):
    async def _handle(self, ctx: discord.ApplicationContext):
        special_cards = (
            ValentineCard
            .select()
            .join(Presenter)
            .join(User)
            .where(
                ValentineCard.is_special == True,
                ValentineCard.do_present == True,
                not ValentineCard.in_process == False,
                User.discord_user_id == ctx.author.id
            )
            .execute()
        )
        
        if len(special_cards) < 1:
            await ctx.respond(embed=EmbedText(ts.can_give_special_card))
