import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils.dataIO import dataIO
from .utils import checks
import asyncio
import textwrap
import os
import math
import aiohttp
from copy import copy

try:
    from PIL import Image, ImageDraw, ImageFont, ImageColor

    pil_available = True
except:
    pil_available = False


class getavatar:
    """snipe dem avatars bruh"""

    def __init__(self, bot):
        self.bot = bot
        self.drawing_settings = fileIO("data/rip/settings.json", "load")

    @commands.command(pass_context=True)
    async def getavatar(self, ctx, user: discord.Member=None):
        """getavatar <user>"""
        avatar_url = user.avatar_url
        avatar_image = Image
        result = Image.open('data/getavatar/blank.jpg').convert('RGBA')
        process = Image.new('RGBA', (500, 500), (0, 0, 0))
        d = ImageDraw.Draw(process)
        try:
            async with aiohttp.get(avatar_url) as r:
                image = await r.content.read()
            with open('data/drawing/temp_avatar', 'wb') as f:
                f.write(image)
                success = True
        except Exception as e:
            success = False
            print(e)
        if success:
            avatar_image = Image.open('data/drawing/temp_avatar').convert('RGBA')
            avatar_image = avatar_image.resize(size=(500, 500))
        d.rectangle([(0, 0), (500, 500)], fill=(0, 0, 0, 0))
        process.paste(avatar_image, (0, 0))
        result = Image.alpha_composite(result, process)
        result.save('data/getavatar/temp.png', 'PNG', quality=100)
        await self.bot.send_file(ctx.message.channel, 'data/getavatar/temp.png')

def setup(bot):
    # check_folders()
    # check_files()
    n = getavatar(bot)
    bot.add_cog(n)