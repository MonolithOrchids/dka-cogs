import discord
from discord.ext import commands
from random import choice as rndchoice
from .utils.dataIO import fileIO
from .utils import checks
import os

    @commands.command(no_pm=True, hidden=True)
    async def moide(self, user : discord.Member, intensity : int=1):
        name = italics(user.display_name)
        if intensity <= 0:
            msg = "moideu{} (￣ω￣) :3".format(name)
        await self.bot.say(msg)

def setup(bot):
    n = moide(bot)
    bot.add_cog(n)