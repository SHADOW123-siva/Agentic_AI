from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv
import os

class EmbeddingManager:
    def __init__(self):
        load_dotenv()
        self.embedding = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
        self.db = Chroma(persist_directory="./memory", embedding_function=self.embedding)
    
    def add_to_memory(self, text):
        self.db.add_texts([text])
        self.db.persist()
        print("🧠 Memory updated and saved.")
