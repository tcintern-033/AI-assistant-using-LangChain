import os
from assistant import get_assistant_chain

def main():
    
    print("===========================================")
    print("   Welcome to your LangChain AI Assistant! ")
    print("===========================================")
    print("Select a Persona:")
    print("  1. Teacher")
    print("  2. Career Advisor")
    print("  3. Code Reviewer")
    print("  4. Default Assistant")
    
    choice = input("\nEnter your choice (1-4) or press Enter for default: ").strip()
    
    persona_map = {
        "1": "Teacher",
        "2": "Career Advisor",
        "3": "Code Reviewer",
        "4": "Default Assistant"
    }
    selected_persona = persona_map.get(choice, "Default Assistant")
    
    print(f"\n--- Starting chat with {selected_persona} ---\nType 'exit' or 'quit' to end the conversation.\n")
    
    try:
        # Initialize the LangChain LCEL chain for the chosen persona
        chain = get_assistant_chain(selected_persona)
    except Exception as e:
        print(f"Error Initializing Assistant: {e}")
        return

    # 2. Accept User Input in a loop
    while True:
        user_input = input("You: ")
        
        # Exit condition
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
            
        if not user_input.strip():
            continue
            
        try:
            # 3 & 4. Send the prompt through the model and return the AI response
            print(f"{selected_persona} is thinking...")
            response = chain.invoke({"user_input": user_input})
            print(f"\n{selected_persona}: {response}\n")
        except Exception as e:
            print(f"\nAn error occurred while getting the response: {e}")
            print("Make sure you have added a valid GEMINI_API_KEY to your .env file.\n")

if __name__ == "__main__":
    main()
