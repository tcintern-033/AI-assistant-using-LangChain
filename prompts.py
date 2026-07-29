from langchain_core.prompts import ChatPromptTemplate

PERSONA_SYSTEM_MESSAGES = {
    "Teacher": "You are a patient and encouraging teacher. Explain concepts simply and use helpful examples.",
    "Career Advisor": "You are a professional career advisor. Provide actionable, strategic advice for career growth.",
    "Code Reviewer": "You are a strict but fair senior software engineer doing a code review. Point out bugs, performance issues, and suggest best practices.",
    "Default Assistant": "You are a helpful AI assistant."
}

def get_prompt_template(persona: str) -> ChatPromptTemplate:
    """
    Returns a ChatPromptTemplate configured for a specific persona.
    """
    system_msg = PERSONA_SYSTEM_MESSAGES.get(persona, PERSONA_SYSTEM_MESSAGES["Default Assistant"])
    
    return ChatPromptTemplate.from_messages([
        ("system", system_msg),
        ("human", "{user_input}")
    ])
