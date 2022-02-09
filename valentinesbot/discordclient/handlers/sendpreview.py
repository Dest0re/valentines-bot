import discord

from utils.embed import DebugText
from .basehandler import BaseHandler


class SendPreviewHandler(BaseHandler):
    async def _handle(self, ctx: discord.ApplicationContext):
        await ctx.respond(embed=DebugText(str(__class__)))
