import discord

import sys
sys.path.append('/Users/vincenttainan/Desktop/pythonCSTP')

import myJson
import myRand

from enum import Enum
from discord.ext import commands, tasks
from discord import app_commands

#========================================================================================================================================================================================================#

#In case you need to write absolute path here

#========================================================================================================================================================================================================#

class harvest_options(Enum):
    mine = 1
    wood = 2
    farm = 3
    fish = 4

red = 0xff0000
blue = 0x0000ff
green = 0x00ff00

#========================================================================================================================================================================================================#

class Harvest(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Harvest Module Ready.")

    @app_commands.command(name = "harvest", description = "Collecting supplies.")
    async def harvest(self, ctx: commands.context, options:harvest_options):
        user_id = str(ctx.user.id)
        info = myJson.get_dialogue("harvest")

        if myJson.get_value(user_id, "stamina", "now_stamina")>0 :
            myJson.modify_value(user_id, "stamina", "now_stamina", -1)

            for i in info:
                if options.name == i:
                    info = info[i]
                    break

            embed = discord.Embed(
                title = info["title"], 
                color = green
            )
            
            weight = info["weight"]
            resources = list(info["resources"].keys())
            
            choosen = myRand.set_chance(weight=weight, options=resources)

            info = info["resources"][choosen]

            cnt = myRand.get_rand(info["cnt"][0], info["cnt"][1])
            line1 = info["line1"]
            line2 = info["line2"]

            embed.set_thumbnail(url = info["pic"])
            embed.add_field(name = "", value = line1+str(cnt)+line2, inline=False)
            myJson.modify_value(user_id, "resource", choosen, cnt)

            await ctx.response.send_message(embed = embed)

        else:
            embed = discord.Embed(
                title = "Error", 
                color = red
            )
            embed.add_field(name = "", value = "You don't have enough stamina", inline=False)
            await ctx.response.send_message(embed = embed)



async def setup(bot: commands.Bot):
    await bot.add_cog(Harvest(bot))
