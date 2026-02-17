from openai import OpenAI
from src.config import get_api_key

def get_client():
    return OpenAI(api_key=get_api_key())

