import re

from generate import generate
from config import model, owner_id
from models.list import model_list
from utils.billing import billing

from utils.splitmsg import split
class commands:
    global model
    async def commands(message):
        if not message.content.startswith("!"):
            return False
        command = message.content[1:].split(" ")[0] if " " in message.content else message.content[1:]
        content = re.sub(f"{command} ", "", message.content[1:]) if " " in message.content else re.sub(f"{command}", "", message.content[1:])
        if command == "model":
            if content == "":
                return "## Models: \n```" + "\n".join(model_list.keys()) + "```"
            else:
                model[str(message.channel.id)] = content[:]
                return f"Model set to {content}"
        if command == "split":
            return await split.split(content)
        if command == "reset":
            await generate.generate("reset", message)
            return "success."
        
        # admin command
        if message.author.id != owner_id:
            return False
        if command == "bal":
            if content.split(" ")[0] == "add":
                res = await billing.balance.add(str(content.split(" ")[1]), float(content.split(" ")[2]))
                return f"Added {content.split(' ')[2]} NT$ to {content.split(' ')[1]}'s balance. He now has {res} NT$ left."
            elif content.split(" ")[0] == "set":
                res = await billing.balance.set(str(content.split(" ")[1]), float(content.split(" ")[2]))
                return f"Set {content.split(' ')[1]}'s balance to {content.split(' ')[2]} NT$."
        else:
            return False