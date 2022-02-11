import discord
from discord.ext import commands

from utils.embed import ErrorText
from utils.strings import text_strings as ts
from discordclient.cogs.debugcog import DebugCog
from discordclient.cogs.giftingcog import GiftingCog


class CollectBotClient(discord.Bot):
    def __init__(self):
        intents = discord.Intents.all()

        super().__init__(intents=intents)

    async def on_ready(self):
        self.add_listener(self.on_command_error)

        print(f'Logged in Discord as {self.user}')

    async def on_command_error(self, ctx: discord.ApplicationContext, error):
        if isinstance(error, commands.errors.PrivateMessageOnly):
            await ctx.respond(embed=ErrorText(ts.only_dm_error), ephemeral=True)


bot = CollectBotClient()

bot.add_cog(DebugCog(bot))
bot.add_cog(GiftingCog(bot))
