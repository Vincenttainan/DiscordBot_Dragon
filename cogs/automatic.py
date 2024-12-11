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
    "bag" : "https://i.imgur.com/RSKeSAD.png",
    "info" : "https://i.imgur.com/nxLJy6N.png"
}

#========================================================================================================================================================================================================#

class Automatic(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.update_energy.start()

    @commands.Cog.listener()
    async def on_ready(self):
        print("Automatic Module Ready.")

    @tasks.loop(minutes=60)
    async def update_energy(self):
        myJson.update_all_stamina()
        




async def setup(bot: commands.Bot):
    await bot.add_cog(Automatic(bot))
