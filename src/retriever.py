from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

class Retriever:
    def __init__(self):
        load_dotenv()
        self.llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
        self.db = Chroma(persist_directory="./memory")
        self.retriever = self.db.as_retriever()

        self.prompt = ChatPromptTemplate.from_template(
            "Use the following context to answer the question.\n\nContext:\n{context}\n\nQuestion: {input}"
        )
        self.combine_docs_chain = create_stuff_documents_chain(self.llm, self.prompt)
        self.retrieval_chain = create_retrieval_chain(self.retriever, self.combine_docs_chain)
    
    def search_memory(self, query):
        result = self.retrieval_chain.invoke({"input": query})
        return result["answer"]
