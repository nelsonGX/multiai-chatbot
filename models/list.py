model_list = {
    "gpt-4-turbo": {
        "provider": "openai",
        "cost": {
            "input": 10,
            "output": 30
        }
    },
    "gpt-4-turbo-preview": {
        "provider": "openai",
        "cost": {
            "input": 10,
            "output": 30
        }
    },
    "gpt-4-0125-preview": {
        "provider": "openai",
        "cost": {
            "input": 30,
            "output": 60
        }
    },
    "gpt-4": {
        "provider": "openai",
        "cost": {
            "input": 30,
            "output": 60
        }
    },
    "gpt-4-32k": {
        "provider": "openai",
        "cost": {
            "input": 60,
            "output": 120
        }
    },
    
    "gpt-3.5-turbo": {
        "provider": "openai",
        "cost": {
            "input": 0.5,
            "output": 1.5
        }
    },
    "gpt-3.5-turbo-instruct": {
        "provider": "openai",
        "cost": {
            "input": 1.5,
            "output": 2
        }
    },


    "claude-3-opus-20240229": {
        "provider": "anthropic",
        "cost": {
            "input": 15,
            "output": 75
        }
    },
    "claude-3-sonnet-20240229": {
        "provider": "anthropic",
        "cost": {
            "input": 3,
            "output": 15
        }
    },
    "claude-3-haiku-20240307": {
        "provider": "anthropic",
        "cost": {
            "input": 0.25,
            "output": 1.25
        }
    },
    "claude-2.1": {
        "provider": "anthropic",
        "cost": {
            "input": 8,
            "output": 24
        }
    },
    "claude-2.0": {
        "provider": "anthropic",
        "cost": {
            "input": 8,
            "output": 24
        }
    },
    

    "gemini-1.5-pro-latest": {
        "provider": "google",
        "cost": {
            "input": 0,
            "output": 0
        }
    },
    "gemini-pro": {
        "provider": "google",
        "cost": {
            "input": 0,
            "output": 0
        }
    },
    

    # "@cf/mistral/mistral-7b-instruct-v0.1": {
    #     "provider": "cloudflare",
    #     "cost": {
    #         "input": 0,
    #         "output": 0
    #     }
    # },
    "@cf/meta/llama-2-7b-chat-fp16": {
        "provider": "cloudflare",
        "cost": {
            "input": 0,
            "output": 0
        }
    },
}

provider_list = {
    "openai": {
        "name": "OpenAI",
        "url": "https://openai.com",
    },
    "anthropic": {
        "name": "Anthropic",
        "url": "https://anthropic.com"
    },
    "google": {
        "name": "Google",
        "url": "https://cloud.google.com"
    },
    "cloudflare": {
        "name": "Cloudflare",
        "url": "https://cloudflare.com"
    }
}

class translate_history:
    class openai:
        async def system(message):
            return {"role": "system", "content": message}
        async def user(message):
            return {"role": "user", "content": message}
        async def model(message):
            return {"role": "assistant", "content": message}
    class anthropic:
        async def system(message):
            return {"role": "system", "content": message}
        async def user(message):
            return {"role": "user", "content": message}
        async def model(message):
            return {"role": "assistant", "content": message}
    class google:
        async def system_1(message):
            return {"role": "user", "parts": [message]}
        async def system_2(message):
            return {"role": "model", "parts": ["understood."]}
        async def user(message):
            return {"role": "user", "parts": [message]}
        async def model(message):
            return {"role": "model", "parts": [message]}
    class cloudflare:
        async def system(message):
            return {"role": "system", "content": message}
        async def user(message):
            return {"role": "user", "content": message}
        async def model(message):
            return {"role": "assistant", "content": message}