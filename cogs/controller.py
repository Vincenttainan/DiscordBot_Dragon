import discord

import sys
sys.path.append('/Users/vincenttainan/Desktop/pythonCSTP')

import myJson
import myRand
import myEmoji

from enum import Enum
from discord.ext import commands, tasks
from discord import app_commands

#========================================================================================================================================================================================================#

red = 0xff0000
blue = 0x0000ff
green = 0x00ff00
white = 0xffffff

#========================================================================================================================================================================================================#

class Controller(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Controller Module Ready.")

    @app_commands.command(name = "add_all_stamina", description = "add all stamina")
    async def bag(self, ctx: commands.context):
        myJson.update_all_stamina()
        embed = discord.Embed(
            title = "Form Controller", 
            color = white
        )
        embed.add_field(name = "Add all stamina", value = "Trigger from Controller/add_all_stamina", inline=False)
        await ctx.response.send_message(embed = embed)





async def setup(bot: commands.Bot):
    await bot.add_cog(Controller(bot))
