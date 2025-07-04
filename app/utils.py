from google import genai
from google.genai import types
from config import gemini_api

def get_gemini_client():
    """Инициализирует и возвращает клиент Gemini API."""
    global _gemini_client
    if _gemini_client is None:
        _gemini_client = genai.Client(api_key=gemini_api)
    return _gemini_client


def return_text(query, system_prompt='ты человек'):

    client = genai.Client(api_key=gemini_api) 

    response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=query,
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(thinking_budget=0),
                system_instruction=system_prompt),
                                                )
    
    return response.text
