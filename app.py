from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY=os.getenv("GROQ_API_KEY")
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.5,
    max_tokens=1024
)
prompt=ChatPromptTemplate.from_messages(
    [
        ("system", "You are an AI assistant that helps to give accurate and concise answers to user's questions in simple language."),
        ("user", "{question}")
    ]
)
parser=StrOutputParser()
chain=prompt|llm|parser
while True:
    user_input=input("User: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chat. Goodbye!")
        break
    response=chain.invoke({"question":user_input})
    print("AI: "+response)



