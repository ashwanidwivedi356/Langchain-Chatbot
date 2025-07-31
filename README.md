# 🧠 LangChain + OpenRouter Chatbot (Terminal-Based)

This is a terminal-based chatbot built using [LangChain](https://github.com/langchain-ai/langchain), [OpenRouter](https://openrouter.ai/), and the Mistral-7B-Instruct model. It supports structured responses using `StructuredOutputParser` and maintains a running chat history.

---

## 🚀 Features

- ✅ Uses **OpenRouter API** with **Mistral-7B-Instruct**
- ✅ Structured replies using `StructuredOutputParser`
- ✅ Memory-like chat history
- ✅ Easy terminal-based interaction
- ✅ Lightweight and easy to extend

---

## 📸 Demo

You: Hello
AI: Hello! How can I assist you today?

You: Tell me a joke
AI: Why don’t scientists trust atoms? Because they make up everything!

yaml
Copy
Edit

---

## 🧰 Tech Stack

- [LangChain](https://python.langchain.com/)
- [OpenRouter API](https://openrouter.ai/)
- Python 3.8+
- Mistral-7B (via OpenRouter)
- `dotenv` for environment variables

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/langchain-openrouter-chatbot.git
cd langchain-openrouter-chatbot
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Create .env File
Create a .env file in the root directory and add your OpenRouter API key:

ini
Copy
Edit
OPENROUTER_API_KEY=your_openrouter_api_key_here
You can get the API key from OpenRouter.ai.

4. Run the Chatbot
bash
Copy
Edit
python chatbot.py
📄 requirements.txt
txt
Copy
Edit
langchain
langchain_openai
python-dotenv
📁 Project Structure
bash
Copy
Edit
.
├── chatbot.py          # Main chatbot script
├── .env                # Environment variables (ignored by Git)
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
🧠 How It Works
Prompts are created with chat history + user input.

A structured output schema (reply) ensures responses follow a fixed format.

History is updated on each turn using SystemMessage, HumanMessage, and AIMessage.

Mistral model is used via OpenRouter for inference.

🛠️ Customization Ideas
Add more fields to ResponseSchema (e.g., emotion, action, summary)

Connect with a frontend using FastAPI or Flask

Add memory support using LangChain Memory components

Save conversations to a file or database

📃 License
MIT License. Feel free to use and modify.

🙋‍♂️ Author
Ashwani Kumar Dwivedi
Open to collaborations!
LinkedIn | GitHub

yaml
Copy
Edit
