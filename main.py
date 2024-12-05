import discord
import myRand
import myJson
import asyncio
import os
from discord.ext import commands
from enum import Enum

#========================================================================================================================================================================================================#

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "!030 ", intents = intents)

#========================================================================================================================================================================================================#

admin=[
    "601255055055781891",   #G8
    "186087112435695617",   #Guo
    "830075334451003422"    #Vincenttainan
]

#========================================================================================================================================================================================================#

@bot.event
async def on_ready():
    try:
        await bot.tree.sync()
        print(f"Commands synced. Now signed in as --> {bot.user}")
    except Exception as e:
        print(f"Error syncing commands: {e}")

async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

#========================================================================================================================================================================================================#

@bot.tree.command(name = "sleep", description = "Shut down!!!")
async def sleep(ctx):
    if str(ctx.user.id) in admin:
        await ctx.response.send_message("Sleeping~")
        await bot.close()
    else:
        await ctx.response.send_message("Go eat yourself")

#========================================================================================================================================================================================================#

class cogs_options(Enum):
    harvest = "harvest"
    none = "none"

@bot.tree.command(name = "reload", description = "reload a cog")
async def reload(ctx, options:cogs_options):
    if str(ctx.user.id) in admin:
        await bot.reload_extension(f"cogs.{options.name}")
        await ctx.response.send_message(f"ReLoaded {options.name} done.")
    else:
        await ctx.response.send_message("Go eat yourself")

@bot.tree.command(name = "load", description = "load a cog")
async def load(ctx, options:cogs_options):
    if str(ctx.user.id) in admin:
        await bot.load_extension(f"cogs.{options.name}")
        await ctx.response.send_message(f"Loaded {options.name} done.")
    else:
        await ctx.response.send_message("Go eat yourself")

@bot.tree.command(name = "unload", description = "unload a cog")
async def unload(ctx, options:cogs_options):
    if str(ctx.user.id) in admin:
        await bot.unload_extension(f"cogs.{options.name}")
        await ctx.response.send_message(f"UnLoaded {options.name} done.")
    else:
        await ctx.response.send_message("Go eat yourself")

#========================================================================================================================================================================================================#

async def main():
    async with bot:
        await load_extensions()
        await bot.start("MTMwNjE5OTAzNTk1NDIwNDY4Mg.Gtulsk.-k96oUchHsS94LIwtm6eelS38XWs3BoyJ5comQ")

#========================================================================================================================================================================================================#

if __name__ == "__main__":
    asyncio.run(main())
