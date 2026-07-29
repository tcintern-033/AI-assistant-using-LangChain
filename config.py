import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

def get_chat_model():
    """
    Returns the configured Chat Model.
    """
    return ChatGoogleGenerativeAI(model="gemini-3.6-flash")
