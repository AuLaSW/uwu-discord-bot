from discord.ext.commands import Bot
from discord.ext import commands

@commands.command()
async def hello(ctx):
    channel = ctx.message.channel
    await channel.send("Hello!")
    
@commands.command()
async def add(ctx, left: int, right: int):
    channel = ctx.message.channel
    sum = left + right
    await channel.send(f'The sum of {left} and {right} is {sum}')
    
def setup(bot):
    bot.add_command(hello)
    bot.add_command(add)
