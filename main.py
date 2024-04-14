import discord
import asyncio

from utils.splitmsg import split
from utils.command import commands
from utils.billing import billing
from generate import generate
from config import discord_token

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'# Logged as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == ("!FORCESTOP"):
        exit()
    
    cmdmsg = await commands.commands(message)
    if cmdmsg != False:
        await message.channel.send(cmdmsg)
        return

    if client.user.mentioned_in(message) or isinstance(message.channel, discord.DMChannel):
        if await billing.balance.get(str(message.author.id)) <= 0.0:
            await message.reply("You don't have any balance left.")
            return
        question = message.content
        if question.startswith(f"<@{client.user.id}>"):
            question = question.replace(f"<@{client.user.id}> ", "")
        print(f"# Prompt: {question}")
        
        async with message.channel.typing():
            try:
                response = await generate.generate(question, message)
            except Exception as e:
                print(e)
                await message.reply("An error occured, please check console log. Use !reset to reset chat history.")
                return

            if isinstance(response, str):
                await message.channel.send(response)
                return

            print("# Response: " + response["message"])
            response_split = await split.split(response["message"])
            for i in response_split:
                await message.channel.send(i)

        msg = await message.channel.send(f"*You spent **{response['cost']}** NT$ / **{response['left']}** NT$ left.*")
        await asyncio.sleep(3)
        await msg.delete()

        return

client.run(discord_token)