from openai import OpenAI

from config import openai_key
from utils.billing import billing

gpt = OpenAI(api_key=openai_key)

async def generate(model, history):
    response = gpt.chat.completions.create(
        model=model,
        messages=history,
        max_tokens=4096
    )
    print(response)

    cost = await billing.cost(model, response.usage.prompt_tokens, response.usage.completion_tokens)

    return {"message": response.choices[0].message.content, "cost": cost}