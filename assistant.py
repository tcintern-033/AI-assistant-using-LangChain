from langchain_core.output_parsers import StrOutputParser
from config import get_chat_model
from prompts import get_prompt_template

def get_assistant_chain(persona: str):
    """
    Returns a LangChain LCEL chain configured for a specific persona.
    """
    model = get_chat_model()
    prompt = get_prompt_template(persona)
    
    # Build the Basic LangChain Workflow (LCEL Chain)
    # The input flows into the prompt, then to the model, and the raw output is parsed as a string.
    chain = prompt | model | StrOutputParser()
    
    return chain
