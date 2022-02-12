import discord

from .abstractbasehandler import AbstractBaseHandler, StopHandleException
from model import ValentineCard, Presenter, User
from utils.embed import ErrorText


class BaseHandler(AbstractBaseHandler):
    async def do_handle(self, ctx: discord.ApplicationContext):
        try:
            await self._handle(ctx)
        except StopHandleException:
            await self._exc(ctx)
        except Exception as e:
            await self._exc(ctx)

            raise e
        else:
            if self._next:
                await self._next.do_handle(ctx)

    async def _exc(self, ctx: discord.ApplicationContext):
        user = User.get_or_none(discord_user_id=ctx.author.id)

        if user:
            presenter = Presenter.get_or_create(user=user)[0]

            card = ValentineCard.get_last_presenter_card_or_none(presenter)

            if card:
                card.in_process = False
                card.save()

        await ctx.respond(embed=ErrorText('Что-то пошло не так... Вам придётся начинать сначала!'))
