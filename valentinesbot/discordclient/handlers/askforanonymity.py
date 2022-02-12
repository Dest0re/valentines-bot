import asyncio

import discord
from discord.ui.select import SelectOption

from utils.embed import DebugText, EmbedText, ErrorText, SuccessText
from .abstractbasehandler import StopHandleException
from .basehandler import BaseHandler
from .view.dropdown import PersonalOneChoiceDropdown
from model import User, ValentineCard, Presenter
from utils.strings import text_strings as ts


class AskForAnonymityHandler(BaseHandler):
    async def _handle(self, ctx: discord.ApplicationContext):
        presenter = Presenter.from_discord_id(ctx.author.id)

        card = ValentineCard.get_last_presenter_card_or_none(presenter)
        normal_emoji = ctx.bot.get_emoji(941994361426690048)
        anonymous_emoji = ctx.bot.get_emoji(941993632041406466)

        if not card:
            raise KeyError()

        dropdown = PersonalOneChoiceDropdown(
            ctx.author,
            ts.anonymity_choice_placeholder,
            options=[
                SelectOption(label="Не анонимно", emoji=normal_emoji),
                SelectOption(label="Анонимно", emoji=anonymous_emoji),
            ]
        )

        message = await ctx.respond(embed=EmbedText(ts.ask_for_anonymity), view=discord.ui.View(dropdown))

        try:
            choice = await dropdown.get_choices(300)
        except asyncio.TimeoutError:
            await ctx.respond(embed=ErrorText(ts.timeout_error))
            raise StopHandleException(str(__class__))

        new_text = "Вы выбрали: " + choice.label

        dropdown.disabled = True
        await message.edit(embed=SuccessText(new_text), view=discord.ui.View(dropdown))

        match choice.label:
            case "Не анонимно":
                card.is_anonymous = False
            case "Анонимно":
                card.is_anonymous = True

        card.save()
