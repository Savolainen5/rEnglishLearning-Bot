import nextcord
from nextcord.ext import commands

#Copied entirely from https://www.youtube.com/watch?v=hoVtbSp-AZ4

class Basic(commands.Cog):
    def __init__(self, bot): #Variables for the init, I think?
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("I'm alive!")

def setup(bot):
    bot.add_cog(Basic(bot))