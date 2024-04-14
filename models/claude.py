from anthropic import Anthropic

from config import anthropic_key
from utils.billing import billing

client = Anthropic(api_key=anthropic_key)

async def generate(model, history):
    message = client.messages.create(
        model=model,
        max_tokens=4096,
        messages=history
    )
    print(message)

    cost = await billing.cost(model, message.usage.input_tokens, message.usage.output_tokens)

    return {"message": message.content[0].text, "cost": cost}