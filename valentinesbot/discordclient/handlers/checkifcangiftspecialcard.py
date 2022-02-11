import discord

from utils.embed import DebugText
from .basehandler import BaseHandler
from model import User, Presenter, ValentineCard


class CheckIfCanGiftSpecialCardHandler(BaseHandler):
    async def _handle(self, ctx: discord.ApplicationContext):
        special_cards = (
            ValentineCard
            .select()
            .join(Presenter)
            .join(User)
            .where(
                ValentineCard.is_special, 
                ValentineCard.do_present, 
                not ValentineCard.in_process, 
                User.discord_user_id == ctx.author.id
            )
            .execute()
        )
        
        if len(special_cards) < 1:
            await ctx.respond(embed=DebugText('Остались специальные валентинки'))
        else:
            await ctx.respond(embed=DebugText('специальных валентинок не осталось'))
