from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found. Please check your .env file.")

llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama-3.3-70b-versatile",
    temperature=0.7
)

def generate_response(prompt):
    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        raise Exception(f"LLM Error: {str(e)}")