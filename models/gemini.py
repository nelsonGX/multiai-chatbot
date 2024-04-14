import google.generativeai as genai

from config import gemini_key
from utils.billing import billing

genai.configure(api_key=gemini_key)

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 4096,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]

async def generate(model, history):
    model = genai.GenerativeModel(model_name=model,
                                generation_config=generation_config,
                                safety_settings=safety_settings)
    response = await model.generate_content_async(history)
    print(response)

    cost = await billing.cost(model, await model.count_tokens_async(history), await model.count_tokens_async(response.text))

    return {"message": response.text, "cost": cost}