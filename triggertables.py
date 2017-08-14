import discord
from __main__ import settings
from random import choice as randchoice

# made by dimxxz https://github.com/dimxxz/dimxxz-Cogs

class poitrigger:
    def __init__(self, bot):
        self.bot = bot
        self.owner = '<!{}>'.format(settings.owner)

    async def listener(self, message):
        channel = message.channel
        if message.author.id != self.bot.user.id:
            if message.content.lower().startswith('(╯°□°）╯︵ ┻━┻'):
                try:
                    await self.bot.send_message(message.channel, '┬─┬﻿ ノ( ゜-゜ノ) ***Please do not flip things... It makes me really upset...***')

                except discord.Forbidden:
                    await self.bot.send_message(message.channel, 'I need permissions~ POOOOOOOOOI >A<')





                
def setup(bot):
    n = poitrigger(bot)
    bot.add_listener(n.listener, "on_message")
    bot.add_cog(n)
