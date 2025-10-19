import time
from src.scraper import WebScraper
from src.cleaner import DataCleaner
from src.embeddings import EmbeddingManager
from src.retriever import Retriever
from src.scheduler import Scheduler

class AutoLearningAgent:
    def __init__(self):
        self.scraper = WebScraper()
        self.cleaner = DataCleaner()
        self.embedder = EmbeddingManager()
        self.retriever = Retriever()
        self.scheduler = Scheduler(self)
    
    def learn(self):
        print("🧠 Learning new data...")
        raw_data = self.scraper.fetch_latest()
        cleaned = self.cleaner.clean(raw_data)
        self.embedder.add_to_memory(cleaned)
        print("✅ Data learned and stored.")
    
    def answer(self, query):
        print(f"❓ Question: {query}")
        result = self.retriever.search_memory(query)
        print(f"💬 Answer: {result}")
    
    def run(self):
        print("🔄 Agent running. Type 'learn' or ask a question (or 'exit').")
        while True:
            user_input = input("\n>>> ").strip().lower()
            if user_input == "exit":
                break
            elif user_input == "learn":
                self.learn()
            else:
                self.answer(user_input)
