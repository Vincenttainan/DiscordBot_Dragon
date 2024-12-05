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
async def hello(ctx):
    await ctx.response.send_message("Sleeping~")
    await bot.close()
#========================================================================================================================================================================================================#

@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded {extension} done.")

@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"UnLoaded {extension} done.")

@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f"cogs.{extension}")
    await ctx.send(f"ReLoaded {extension} done.")

#========================================================================================================================================================================================================#

async def main():
    async with bot:
        await load_extensions()
        await bot.start("MTMwNjE5OTAzNTk1NDIwNDY4Mg.Gtulsk.-k96oUchHsS94LIwtm6eelS38XWs3BoyJ5comQ")

#========================================================================================================================================================================================================#

if __name__ == "__main__":
    asyncio.run(main())
