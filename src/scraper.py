import requests
from bs4 import BeautifulSoup

class WebScraper:
    def fetch_latest(self, url="https://news.ycombinator.com/"):
        print(f"🌐 Fetching data from {url}")
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        titles = [t.get_text() for t in soup.select(".titleline a")]
        return " ".join(titles)
