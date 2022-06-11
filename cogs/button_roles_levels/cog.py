from .level_role_view import LevelRoleView
from nextcord.ext import commands

class LevelRolesCog(commands.Cog, name="Button roles test"):
    #Creates buttons that assign roles

    def __init__(self, bot: commands.Bot):
        self.__bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        #Called when the bot is loaded, apparently
        self.__bot.add_view(LevelRoleView())
        print("Button view added")

    @commands.command()
    @commands.is_owner()
    async def levels(self, ctx: commands.Context):
        #Creates a new role view
        await ctx.send("Click a button to add or remove a role.", view=LevelRoleView())

#class ButtonTestRolesCog(commands.Cog, name="Test role button cog"):
    #Creates buttons that assign roles

#    def __init__(self, bot: commands.Bot):
#        self.__bot = bot

#    @commands.Cog.listener()
#    async def on_ready(self):
        #Called when the bot is loaded, apparently
#        self.__bot.add_view(TestRoleView())
#        print("Test role button view added")

#    @commands.command()
#    @commands.is_owner()
#    async def test_roles(self, ctx: commands.Context):
        #Creates a new role view
#        await ctx.send("Click a button to add or remove a role.", view=TestRoleView())

# setup functions for bot
def setup(bot):
    bot.add_cog(LevelRolesCog(bot))
#    bot.add_cog(ButtonTestRolesCog(bot))