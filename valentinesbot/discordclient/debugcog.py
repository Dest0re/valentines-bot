import discord
from discord.commands import SlashCommandGroup, slash_command

from .basecog import BaseCog


class DebugCog(BaseCog):
    debug_group = SlashCommandGroup(
        'debug',
        'Debug features, Admin only!',
        guild_ids=[940568693723783230]
    )

    @debug_group.command(name='ping', description='Send "Pong" message')
    async def _ping_command(self, ctx: discord.ApplicationContext):
        await ctx.respond('Pong!')
