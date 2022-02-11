import discord

from utils.embed import DebugText
from .basehandler import BaseHandler
from .abstractbasehandler import StopHandleException
from model import User


class RegisterSimpleUserHandler(BaseHandler):
    async def _handle(self, ctx: discord.ApplicationContext):
        user = User.get_or_create(discord_user_id=ctx.author.id)[0]
