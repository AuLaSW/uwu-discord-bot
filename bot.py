"""
Bot.py
------

This application creates a simple and generic Discord Bot.
"""
import os
import discord
from dotenv import load_dotenv
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

import uwu


load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL = os.getenv('CHANNEL')


def intentsFunc(base="none", **kwargs) -> discord.Intents:
    """
    This is a method for cleaning up intents setting.

    Accepts a dictionary of intents, where the keys
    are the different intents and the values are boolean.
    """
    intents = getattr(discord.Intents, base, "default")()

    for intent, value in kwargs.items():
        try:
            setattr(intents, intent, value)
        except AttributeError as e:
            raise e

    return intents


class Botty2_0(Bot):
    """
    Another example of a bot
    """
    async def on_ready(self):
        print(f'{self.user}, the Bot, is ready to go!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.channel.name != CHANNEL:
            return

        print("Message received! Uwuifying...")

        text = message.content
        user = message.author

        text = uwu.uwuify(text)

        await message.channel.send(f"<@{user.id}> said:\n\n" + text)

        await message.delete(delay=0.2)


def main():
    intentdict = {}
    intentdict["messages"] = True
    intentdict["message_content"] = True
    intentdict["guilds"] = True
    intents = intentsFunc("none", **intentdict)

    bot = Botty2_0(command_prefix="\\", intents=intents)

    # General.setup(bot)

    bot.run(TOKEN)


if __name__ == "__main__":
    main()
