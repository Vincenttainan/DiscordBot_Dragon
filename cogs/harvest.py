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

photos = {
    # all of the photos are needed to be redrawed with the size of 320 x 320 (pixels) or maybe 16 x 16 blocks (20 pixels for a block)
    "coal" : "https://i.imgur.com/iqfXcRG.png",
    "gold" : "https://i.imgur.com/voH559P.png",
    "crystal" : "https://i.imgur.com/b7u9Olw.png",
    "branch" : "https://i.imgur.com/PT7QYZ9.png",
    "bark" : "https://i.imgur.com/gxowpyc.png",
    "resin" : "https://i.imgur.com/Ynb5X7M.png",
    "beef" : "https://i.imgur.com/XklB9eo.png",
    "lamb" : "https://i.imgur.com/t84sqCd.png",
    "lizard" : "https://i.imgur.com/3GUUPWe.png",
    "salmon" : "https://i.imgur.com/BLaYsC7.png",
    "cod" : "https://i.imgur.com/tnvWUxy.png",
    "pufferfish" : "https://i.imgur.com/aBZthLA.png"

}

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
        _rand = myRand.get_rand(1, 100)

        if options.name == "mine":
            embed = discord.Embed(
                title = "Mining", 
                color = green
            )

            if _rand <= 50:
                cnt = myRand.get_rand(3, 5)
                embed.set_thumbnail(url = photos["coal"])
                embed.add_field(name = "", value = "After a long long mining\nYou finally found a pile of coal\nYou obtain `"+str(cnt)+"` lumps of `coal`", inline=False)
                myJson.modify_value(user_id, "resource", "coal", cnt)
            elif _rand <= 90:
                cnt = myRand.get_rand(2, 3)
                embed.set_thumbnail(url = photos["gold"])
                embed.add_field(name = "", value = "You accidentally dug into a dragon nest\nBut lucky, the owner wasn't there\nYou grabbed `"+str(cnt)+"` ingots of `gold` and ran away", inline=False)
                myJson.modify_value(user_id, "resource", "gold", cnt)
            else:
                cnt = myRand.get_rand(1, 3)
                embed.set_thumbnail(url = photos["crystal"])
                embed.add_field(name = "", value = "You fell into a canyon unexpectedly\nYou felt wet in pants while a stalagmite almost penetrate you\nYou found `"+str(cnt)+"` blocks of `crystal` beside the stalagmite", inline=False)
                myJson.modify_value(user_id, "resource", "crystal", cnt)

            await ctx.response.send_message(embed = embed)

        elif options.name == "wood":
            embed = discord.Embed(
                title = "Wooding", 
                color = green
            )

            if _rand <= 50:
                cnt = myRand.get_rand(3, 5)
                embed.set_thumbnail(url = photos["branch"])
                embed.add_field(name = "", value = "After a long search through the woods\nYou finally found a robust tree\nSawing off the trunk and received `"+str(cnt)+"` branchs of `branch`", inline=False)
                myJson.modify_value(user_id, "resource", "branch", cnt)
            elif _rand <= 90:
                cnt = myRand.get_rand(2, 3)
                embed.set_thumbnail(url = photos["bark"])
                embed.add_field(name = "", value = "Walking for a whole morning gained for nothing\nYou cut off some tree barks so as not to gain nothing\nYou leave depressedly with `"+str(cnt)+"` piles of `bark`", inline=False)
                myJson.modify_value(user_id, "resource", "bark", cnt)
            else:
                cnt = myRand.get_rand(1, 3)
                embed.set_thumbnail(url = photos["resin"])
                embed.add_field(name = "", value = "Seeing a massive sacred tree, you ran toward it\nFinding too huge to cut off\nBottled the liquid it dropped and gained `"+str(cnt)+"` glasses of `resin`", inline=False)
                myJson.modify_value(user_id, "resource", "resin", cnt)

            await ctx.response.send_message(embed = embed)

        elif options.name == "farm":
            embed = discord.Embed(
                title = "Farming", 
                color = green
            )

            if _rand <= 40:
                cnt = myRand.get_rand(4, 6)
                embed.set_thumbnail(url = photos["beef"])
                embed.add_field(name = "", value = "Driving cattle to graze for the whole day\nDiscovered a seriously injured ox lying beside a river\nYou ended his suffering and cut of `"+str(cnt)+"` cubes if `beef`", inline=False)
                myJson.modify_value(user_id, "resource", "beef", cnt)
            elif _rand <= 80:
                cnt = myRand.get_rand(2, 3)
                embed.set_thumbnail(url = photos["lamb"])
                embed.add_field(name = "", value = "Baa Baa Baa\nYou found a flock of sheep\nAnd obtain `"+str(cnt)+"` cubes of `lamb`", inline=False)
                myJson.modify_value(user_id, "resource", "lamb", cnt)
            else:
                cnt = 1
                embed.set_thumbnail(url = photos["lizard"])
                embed.add_field(name = "", value = "A flash before your eyes\nYou chased the sudden moving for a period\nAnd found `"+str(cnt)+"` `lizard` hiding itself under a rock", inline=False)
                myJson.modify_value(user_id, "resource", "lizard", cnt)

            await ctx.response.send_message(embed = embed)

        elif options.name == "fish":
            embed = discord.Embed(
                title = "Fishing", 
                color = green
            )

            if _rand <= 40:
                cnt = myRand.get_rand(4, 6)
                embed.set_thumbnail(url = photos["salmon"])
                embed.add_field(name = "", value = "Casting your line into a rapid stream, you feel a strong tug\nAfter a fierce struggle, you pull up a sleek salmon\nYou caught `"+str(cnt)+"` `salmon`", inline=False)
                myJson.modify_value(user_id, "resource", "salmon", cnt)
            elif _rand <= 80:
                cnt = myRand.get_rand(2, 3)
                embed.set_thumbnail(url = photos["cod"])
                embed.add_field(name = "", value = "Riding the wind and waves\nYou spot a school of cod gliding through the deep waters\nWith some patience, you manage to catch `"+str(cnt)+"` big fat `cod`", inline=False)
                myJson.modify_value(user_id, "resource", "cod", cnt)
            else:
                cnt = 1
                embed.set_thumbnail(url = photos["pufferfish"])
                embed.add_field(name = "", value = "After a long wait, you reel in a pufferfish\nIts bloated form and venomous spines make it a risky catch\nYou secure `"+str(cnt)+"` spiky `pufferfish`", inline=False)
                myJson.modify_value(user_id, "resource", "pufferfish", cnt)

            await ctx.response.send_message(embed = embed)





async def setup(bot: commands.Bot):
    await bot.add_cog(Harvest(bot))
