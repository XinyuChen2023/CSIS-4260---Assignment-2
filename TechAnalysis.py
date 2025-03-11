import scrapy
import pandas as pd
from textblob import TextBlob
from gensim.summarization.summarizer import summarize

class TechAnalysis:
    def __init__(self, articles):
        self.articles = articles

    def summarize_text(self, text):
        """Summarizes the article text."""
        return summarize(text, ratio=0.2) if len(text.split()) > 50 else text

    def get_sentiment(self, text):
        """Assigns sentiment score (-1 to 1) and converts to importance (-10 to 10)."""
        sentiment = TextBlob(text).sentiment.polarity
        return round(sentiment * 10, 2)

    def analyze(self):
        """Creates a table with analysis results."""
        results = []
        for article in self.articles:
            summary = self.summarize_text(article['text'])
            score = self.get_sentiment(summary)
            results.append({
                "Title": article['title'],
                "Summary": summary,
                "Importance Score": score
            })
        return pd.DataFrame(results)

# Example Usage (Replace with actual scraped data)
articles = [
    {"title": "Tech Innovation in 2025", "text": "Technology is advancing rapidly... (full article)"},
    {"title": "Privacy Concerns in AI", "text": "Many experts warn about data misuse... (full article)"}
]

analysis = TechAnalysis(articles)
df = analysis.analyze()
print(df)
