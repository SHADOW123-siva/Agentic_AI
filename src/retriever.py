from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Chroma
from dotenv import load_dotenv
import os

class Retriever:
    def __init__(self):
        load_dotenv()
        self.llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), temperature=0)
        self.db = Chroma(persist_directory="./memory")
        self.retriever = self.db.as_retriever()
        self.qa_chain = RetrievalQA.from_chain_type(
            self.llm, retriever=self.retriever, chain_type="stuff"
        )
    
    def search_memory(self, query):
        return self.qa_chain.run(query)
