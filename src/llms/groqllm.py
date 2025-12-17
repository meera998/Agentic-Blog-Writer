from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

class GroqLLM:
    def __init__(self):
        load_dotenv()

    def get_llm(self):
        try:
            print(os.getenv("GOOGLE_API_KEY"))
            os.environ["GOOGLE_API_KEY"]=self.google_api_key=os.getenv("GOOGLE_API_KEY")
            llm = ChatGoogleGenerativeAI(
                model="gemini-2.5-flash",
                google_api_key=self.google_api_key
            )
            return llm

        except Exception as e:
            raise ValueError(f"Error occurred while initializing Gemini LLM: {e}")
         