import os
import nextcord
from nextcord.ext import commands
import config
from config import BOT_INTENTS
from config import BOT_TOKEN

#Intents are only needed for using prefix/text commands and not slash commands
#bot = commands.Bot(command_prefix=config.PREFIX, intents=nextcord.Intents().all())
client = commands.Bot(command_prefix=config.PREFIX, intents=BOT_INTENTS)

#To tell me the bot is active
@client.event
async def on_ready():
	print(f"{client.user} has connected to Discord.")

#Load any .py files in the cogs folder, but only directly in the folder
#for fn in os.listdir("./cogs"):
#	if fn.endswith(".py"):
#		bot.load_extension(f"cogs.{fn[:-3]}")

    # load all cogs
for folder in os.listdir("cogs"):
    if os.path.exists(os.path.join("cogs", folder, "cog.py")):
        client.load_extension(f"cogs.{folder}.cog")

#Commands to enable, disable, reload extensions
@client.command()
async def load(ctx, extension):
	client.load_extension(f"cogs.{extension}")
	await ctx.send("Loaded cog!")

@client.command()
async def unload(ctx, extension):
	client.unload_extension(f"cogs.{extension}")
	await ctx.send("Unloaded cog!")

@client.command()
async def reload(ctx, extension):
	client.reload_extension(f"cogs.{extension}")
	await ctx.send("Reloaded cog!")

#To see if the bot is actually reading anything
#@bot.command()
#async def hello(ctx):
#	await ctx.send("Hi")

#bot.run(config.BOT_TOKEN)
client.run(BOT_TOKEN)