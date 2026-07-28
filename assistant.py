import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def get_assistant_chain(persona: str):
    """
    Returns a LangChain LCEL chain configured for a specific persona.
    """
    model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")
    
    # Experimenting with different Prompt Templates based on the persona
    if persona == "Teacher":
        system_msg = "You are a patient and encouraging teacher. Explain concepts simply and use helpful examples."
    elif persona == "Career Advisor":
        system_msg = "You are a professional career advisor. Provide actionable, strategic advice for career growth."
    elif persona == "Code Reviewer":
        system_msg = "You are a strict but fair senior software engineer doing a code review. Point out bugs, performance issues, and suggest best practices."
    else:
        system_msg = "You are a helpful AI assistant."
        
    # Create the Prompt Template
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_msg),
        ("human", "{user_input}")
    ])
    
    # Build the Basic LangChain Workflow (LCEL Chain)
    # The input flows into the prompt, then to the model, and the raw output is parsed as a string.
    chain = prompt | model | StrOutputParser()
    
    return chain
