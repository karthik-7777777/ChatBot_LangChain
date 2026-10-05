# 🤖 LangChain Groq Chatbot

A simple AI chatbot built with **LangChain** and **Groq**, using the **GPT-OSS-20B** model for fast and concise responses.

## 🛠️ Tech Stack

* Python
* LangChain
* Groq
* GPT-OSS-20B
* python-dotenv

## ⚙️ Setup

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

Run the chatbot:

```bash
python app.py
```

## 🔗 LangChain Pipeline

```text
User Input
    ↓
ChatPromptTemplate
    ↓
ChatGroq
    ↓
StrOutputParser
    ↓
AI Response
```

The project demonstrates basic **LangChain LCEL**, prompt templates, LLM integration, and output parsing.

## 👨‍💻 Author

**Karthik K**
