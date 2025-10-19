import re

class DataCleaner:
    def clean(self, text):
        print("🧹 Cleaning text...")
        text = re.sub(r'\s+', ' ', text)
        text = text.strip()
        return text
