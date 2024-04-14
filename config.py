import os
from dotenv import load_dotenv

load_dotenv()

def __init__():
    global model
    global chistory
    global cost
    global balance
    global dprompt
    global discord_token
    global openai_key
    global anthropic_key
    global gemini_key
    global cloudflare_key
    global cloudflare_account_id
    global default_money
    global owner_id

model = {}
chistory = {}
cost = {}
dprompt = {}
balance = {}

discord_token = os.getenv("BOTTOKEN")
openai_key = os.getenv("OPENAIKEY")
anthropic_key = os.getenv("ANTHROPICKEY")
gemini_key = os.getenv("GEMINI_API_KEY")
cloudflare_key = os.getenv("CF_API_KEY")
cloudflare_account_id = os.getenv("CF_ACC_ID")
default_money = float(os.getenv("DEFAULT_MONEY"))
owner_id = os.getenv("OWNER")