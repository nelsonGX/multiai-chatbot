import aiohttp

from config import cloudflare_key, cloudflare_account_id
from utils.billing import billing

API_BASE_URL = f"https://api.cloudflare.com/client/v4/accounts/{cloudflare_account_id}/ai/run/"
headers = {"Authorization": f"Bearer {cloudflare_key}"}


async def run(model, inputs):
    input = { "messages": inputs }
    async with aiohttp.ClientSession() as session:
        response = await session.post(url=f"{API_BASE_URL}{model}", headers=headers, json=input)
    return await response.json()

async def generate(model, history):
    response = await run(model, history)
    print(response)

    cost = await billing.cost(model, len(history), len(response["result"]["response"]))

    return {"message": response["result"]["response"], "cost": cost}