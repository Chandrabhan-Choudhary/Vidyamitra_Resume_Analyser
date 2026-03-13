import os
from dotenv import load_dotenv

load_dotenv()

AI_PROVIDER = os.getenv("AI_PROVIDER")

# ---------- OpenAI ----------
from openai import OpenAI

openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ---------- Gemini ----------
import google.generativeai as genai

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

# Detect available Gemini models
def get_model_name(keyword):
    for m in genai.list_models():
        if "generateContent" in m.supported_generation_methods:
            if keyword in m.name:
                return m.name
    return None

try:
    FLASH_MODEL_NAME = get_model_name("flash")
except:
    FLASH_MODEL_NAME = "models/gemini-1.5-flash-001"

if not FLASH_MODEL_NAME:
    FLASH_MODEL_NAME = "models/gemini-1.5-flash-001"

gemini_model = genai.GenerativeModel(FLASH_MODEL_NAME)


def generate_response(prompt):

    if AI_PROVIDER == "openai":

        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content


    elif AI_PROVIDER == "gemini":

        response = gemini_model.generate_content(prompt)

        return response.text