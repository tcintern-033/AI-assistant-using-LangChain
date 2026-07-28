# LangChain AI Assistant

A simple, interactive command-line AI assistant built using the LangChain framework and Google's Gemini API. This project demonstrates core LangChain concepts such as **Chat Models**, **Prompt Templates**, **Output Parsers**, and **LCEL (LangChain Expression Language)**.

## 🚀 Features

- **Interactive CLI Interface**: Chat continuously in a conversational loop.
- **Multiple Personas**: Switch between different behavior profiles (Teacher, Career Advisor, Code Reviewer) to see how Prompt Templates steer the AI's behavior.
- **Modular Architecture**: Clean separation between application logic (`assistant.py`) and user interaction (`main.py`).
- **Environment Management**: Secure API key management via `.env`.

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.9+
- A valid Google Gemini API Key

## 📦 Installation & Setup

1. **Clone or Download the Repository**
   Ensure you are in the project folder.

2. **Set up a Virtual Environment** (Recommended)
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. **Install Dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Configure your Environment Variables**
   - Rename `.env.example` to `.env` (if you haven't already).
   - Add your API key to the `.env` file:
     ```env
     GEMINI_API_KEY=your_actual_api_key_here
     ```

## 🎮 Usage

Start the interactive assistant by running:

```powershell
python main.py
```

1. **Select a Persona**: The assistant will prompt you to choose an interaction style (e.g., enter `1` for Teacher).
2. **Chat**: Type your queries.
3. **Exit**: Type `exit` or `quit` when you are done.

## 📂 Project Structure

```
.
├── assistant.py       # Core LangChain logic (Models, Templates, LCEL Chains)
├── main.py            # CLI entry point and user interaction loop
├── requirements.txt   # Python dependencies
├── .env               # Secret API keys (ignored by git)
└── .gitignore         # Defines files that Git should ignore
```

## 📚 What I learned
This project served as a playground to learn:
- **How to initialize Chat Models** (`ChatGoogleGenerativeAI`).
- **How to use Prompt Templates** to instruct the LLM programmatically without hardcoding strings.
- **How to pipeline operations** efficiently using the `|` syntax in LCEL.

---
*Built as part of the AI Engineering Track (Introduction to LangChain).*
