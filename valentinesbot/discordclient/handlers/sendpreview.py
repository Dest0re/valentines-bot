import asyncio

import discord

from utils.embed import DebugText, EmbedText, ErrorText
from .abstractbasehandler import StopHandleException
from .basehandler import BaseHandler
from model import ValentineCard, User, Presenter
from utils.strings import text_strings as ts
from .view.button import PersonalYesOrNoButtonsView


def generate_embed(ctx: discord.ApplicationContext, card: ValentineCard, final=False) -> discord.Embed:
    if not card.is_special:
        title = 'Валентинка'
    else:
        title = 'Особенная валентинка!'

    if card.is_anonymous:
        author_name = '???'
        author_avatar_url = None
    else:
        author = ctx.bot.get_user(card.presenter.user.discord_user_id)
        author_name = discord.utils.escape_markdown(str(author))
        author_avatar_url = str(author.avatar.url)

    embed = discord.Embed(color=0xb00b69, title=title, description=card.content, timestamp=card.created_at)
    if author_avatar_url:
        embed.set_author(name=author_name, icon_url=author_avatar_url)
    else:
        embed.set_author(name=author_name)

    return embed


class SendPreviewHandler(BaseHandler):
    async def _handle(self, ctx: discord.ApplicationContext):
        presenter = Presenter.from_discord_id(ctx.author.id)
        card = ValentineCard.get_last_presenter_card_or_none(presenter)

        view = PersonalYesOrNoButtonsView(member=ctx.author)

        message = await ctx.respond(
            embeds=[
                EmbedText(ts.preview_text),
                generate_embed(ctx, card)
            ],
            view=view
        )

        try:
            result = await view.wait_for_result(300)
        except asyncio.TimeoutError:
            await ctx.respond(embed=ErrorText(ts.timeout_error))
            raise StopHandleException(str(__class__))

        for children in view.children:
            children.disabled = True

        await message.edit(embeds=[
                EmbedText(ts.preview_text),
                generate_embed(ctx, card)
            ],
            view=view
        )

        if result:
            card.do_present = True
            card.save()
        else:
            await ctx.respond(embed=EmbedText(ts.card_denied))
            raise StopHandleException(str(__class__))
