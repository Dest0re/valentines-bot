import discord

from utils.embed import DebugText, WarningText, ErrorText
from .abstractbasehandler import StopHandleException
from .basehandler import BaseHandler
from model import ValentineCard, Presenter, User
from utils.strings import text_strings as ts


class CheckIfCannotGiftSpecialCardHandler(BaseHandler):
    async def _handle(self, ctx: discord.ApplicationContext):
        user = User.get_or_none(discord_user_id=ctx.author.id)

        if not user:
            raise StopHandleException(str(__class__))

        presenter = Presenter.get_or_create(user=user)[0]

        cards = (
            ValentineCard
            .select()
            .where(
                ValentineCard.presenter == presenter,
                ValentineCard.is_special == True,
                ValentineCard.in_process == False,
                ValentineCard.do_present == True
            )
            .execute()
        )

        if len(tuple(cards)) > 0:
            await ctx.respond(embed=ErrorText(ts.cannot_give_special_card))
            raise StopHandleException(str(__class__))
