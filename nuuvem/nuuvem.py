from discord.ext import commands

class Nuuvem:
    """Procure por jogos na maior revendedora de jogos no Brasil"""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def nuuvem(self, *text):
        """Busca pelo jogo na Nuuvem, maior revendedora de jogos do Brasil"""

        text = " ".join(text)
        query=text.replace(" ", "%20")
        await self.bot.say("https://www.nuuvem.com/catalog/search/"+query)

def setup(bot):
    n = Nuuvem(bot)
    bot.add_cog(n)
