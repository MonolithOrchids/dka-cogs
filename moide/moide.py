import discord
from discord.ext import commands
from .utils.chat_formatting import escape_mass_mentions, italics, pagify
from random import choice as rndchoice
from random import randint
import os

class Moide:
    """Moide :3."""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(pass_context=True, invoke_without_command=True)
    async def moide(self, ctx, *, user: discord.Member=None):
        """Moide alguém."""
        botid = self.bot.user.id
        if user is None:
            user = ctx.message.author
            await self.bot.say("Vou te moide " + user.name)
        elif user.id == botid:
            user = ctx.message.author
            botname = self.bot.user.name
            await self.bot.say(botname + " Moideu " + user.mention +
                               " :3 ")
        else:
            await self.bot.say("Moideu " + user.name + " :3 ")

def setup(bot):
    n = Moide(bot)
    bot.add_cog(n)
