from models import gpt, claude, gemini, cloudflare
from models.list import translate_history, model_list
from utils.billing import billing

from config import model, chistory

"""
history format:
[
    {"role": "user", "content": "Hello, how are you?"},
    {"role": "model", "content": "I am well, thank you."}
]

"""

class generate:
    global model
    global chistory
   
    async def translate_history_generate(channel, model):
        history = []
        provider = model_list[model]["provider"]
        if provider == "openai":
            for item in chistory[channel]:
                if item["role"] == "user":
                    history.append(await translate_history.openai.user(item["content"]))
                elif item["role"] == "model":
                    history.append(await translate_history.openai.model(item["content"]))
                else:
                    history.append(await translate_history.openai.system(item["content"]))
        elif provider == "anthropic":
            for item in chistory[channel]:
                if item["role"] == "user":
                    history.append(await translate_history.anthropic.user(item["content"]))
                elif item["role"] == "model":
                    history.append(await translate_history.anthropic.model(item["content"]))
                else:
                    history.append(await translate_history.anthropic.system(item["content"]))
        elif provider == "google":
            for item in chistory[channel]:
                if item["role"] == "user":
                    history.append(await translate_history.google.user(item["content"]))
                elif item["role"] == "model":
                    history.append(await translate_history.google.model(item["content"]))
                else:
                    history.append(await translate_history.google.system_1(item["content"]))
                    history.append(await translate_history.google.system_2(item["content"]))
        elif provider == "cloudflare":
            for item in chistory[channel]:
                if item["role"] == "user":
                    history.append(await translate_history.cloudflare.user(item["content"]))
                elif item["role"] == "model":
                    history.append(await translate_history.cloudflare.model(item["content"]))
                else:
                    history.append(await translate_history.cloudflare.system(item["content"]))
        return history


    async def generate(question, message):
        channel = str(message.channel.id)
        user = str(message.author.id)

        async def reset(channel):
            chistory.pop(channel, None)
            return "History reset."
        
        if question == "reset":
            await reset(channel)
            return "History reset."
 
        if channel not in model:
            return "Model not set. Use `!model <model>` to set."
        
        cmodel = model[channel]
        provider = model_list[model[channel]]["provider"]

        if channel not in chistory:
            await reset(channel)
            chistory[channel] = []
        elif chistory[channel][-1]["role"] == "user":
            return "Model did not respond to last message. Please wait for a response."

        chistory[channel].append({"role": "user", "content": question})
        history = await generate.translate_history_generate(channel, model[channel])

        print(history)

        if not provider:
            return "Model not found."
        if provider == "openai":
            reply = await gpt.generate(cmodel, history)
        elif provider == "anthropic":
            reply = await claude.generate(cmodel, history)
        elif provider == "google":
            reply = await gemini.generate(cmodel, history)
        elif provider == "cloudflare":
            reply = await cloudflare.generate(cmodel, history)

        left = await billing.balance.add(user, -1 * reply["cost"])

        chistory[channel].append({"role": "model", "content": reply["message"]})
        return {"message": reply["message"], "cost": reply["cost"], "left": left}