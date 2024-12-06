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


photos = {
    # all of the photos are needed to be redrawed with the size of 320 x 320 (pixels) or maybe 16 x 16 blocks (20 pixels for a block)
    "bag" : "https://i.imgur.com/RSKeSAD.png"
}


#========================================================================================================================================================================================================#

class Bag(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bag Module Ready.")

    @app_commands.command(name = "bag", description = "Seeking items in your bag.")
    async def bag(self, ctx: commands.context):
        user_id = str(ctx.user.id)
        
        embed = discord.Embed(
            title = "<@"+user_id+"> 's bag", 
            color = green
        )

        embed.set_thumbnail(url = photos["bag"])

        embed.add_field(name = "Mine", value = "", inline=False)
        embed.add_field(name = str(myEmoji.emoji_list["coal"]), value = "Coal : `"+str(myJson.get_value(user_id,"resource","coal"))+"`", inline=True)
        embed.add_field(name = str(myEmoji.emoji_list["gold"]), value = "Gold : `"+str(myJson.get_value(user_id,"resource","gold"))+"`", inline=True)
        embed.add_field(name = str(myEmoji.emoji_list["crystal"]), value = "Crystal : `"+str(myJson.get_value(user_id,"resource","crystal"))+"`", inline=True)

        embed.add_field(name = "Wood", value = "", inline=False)
        embed.add_field(name = str(myEmoji.emoji_list["branch"]), value = "Branch : `"+str(myJson.get_value(user_id,"resource","branch"))+"`", inline=True)
        embed.add_field(name = str(myEmoji.emoji_list["bark"]), value = "Bark : `"+str(myJson.get_value(user_id,"resource","bark"))+"`", inline=True)
        embed.add_field(name = str(myEmoji.emoji_list["resin"]), value = "Resin : `"+str(myJson.get_value(user_id,"resource","resin"))+"`", inline=True)

        embed.add_field(name = "Farm", value = "", inline=False)
        embed.add_field(name = str(myEmoji.emoji_list["beef"]), value = "Beef : `"+str(myJson.get_value(user_id,"resource","beef"))+"`", inline=True)
        embed.add_field(name = str(myEmoji.emoji_list["lamb"]), value = "Lamb : `"+str(myJson.get_value(user_id,"resource","lamb"))+"`", inline=True)
        embed.add_field(name = str(myEmoji.emoji_list["lizard"]), value = "Lizard : `"+str(myJson.get_value(user_id,"resource","lizard"))+"`", inline=True)

        embed.add_field(name = "Fish", value = "", inline=False)
        embed.add_field(name = str(myEmoji.emoji_list["salmon"]), value = "Salmon : `"+str(myJson.get_value(user_id,"resource","salmon"))+"`", inline=True)
        embed.add_field(name = str(myEmoji.emoji_list["cod"]), value = "Cod : `"+str(myJson.get_value(user_id,"resource","cod"))+"`", inline=True)
        embed.add_field(name = str(myEmoji.emoji_list["pufferfish"]), value = "Pufferfish : `"+str(myJson.get_value(user_id,"resource","pufferfish"))+"`", inline=True)

        await ctx.response.send_message(embed = embed)


class Info(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Info Module Ready.")

    @app_commands.command(name = "info", description = "Check your infomations.")
    async def info(self, ctx: commands.context):
        user_id = str(ctx.user.id)

        embed = discord.Embed(
                title = "<@"+user_id+"> 's infomations", 
                color = green
            )

        embed.set_thumbnail(url = photos["bag"])

        embed.add_field(name = "Stamina", value = "", inline=False)
        embed.add_field(name = "", value = "Your stamina : `"+str(myJson.get_value(user_id,"stamina","now_stamina"))+"` / "+str(myJson.get_value(user_id,"stamina","max_stamina")), inline=True)

        embed.add_field(name = "Currency", value = "", inline=False)
        embed.add_field(name = "", value = "Emerald : `"+str(myJson.get_value(user_id,"currency","emerald"))+"`", inline=True)
        embed.add_field(name = "", value = "Ruby : `"+str(myJson.get_value(user_id,"currency","ruby"))+"`", inline=True)

        await ctx.response.send_message(embed = embed)





async def setup(bot: commands.Bot):
    await bot.add_cog(Bag(bot))
    await bot.add_cog(Info(bot))
