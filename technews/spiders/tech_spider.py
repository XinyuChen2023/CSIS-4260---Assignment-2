import scrapy
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from tabulate import tabulate

class TechSpider(scrapy.Spider):
    name = "tech_spider"
    allowed_domains = ["arstechnica.com"]
    start_urls = ["https://arstechnica.com/tech-policy/"]

    def parse(self, response):
        articles = response.css('article')
        data = []
        for article in articles:
            title = article.css('h2 a::text').get()
            link = article.css('h2 a::attr(href)').get()
            importance_score = float(np.random.uniform(0.8, 1.5))  # Convert NumPy float to standard Python float
            
            # Append to list for display
            data.append([title, importance_score])

            # Yield the scraped data
            yield {
                'title': title,
                'link': link,
                'importance_score': importance_score
            }

        # Print results in a tabulated format
        headers = ["Article Title", "Importance Score"]
        print(tabulate(data, headers=headers, tablefmt="grid"))

    def compute_tfidf_scores(self):
        """ Uses TF-IDF to rank articles based on keyword importance. """
        if not self.titles:
            return {}

        vectorizer = TfidfVectorizer(stop_words="english")
        tfidf_matrix = vectorizer.fit_transform(self.titles)

        # Compute mean TF-IDF score for each title
        scores = np.mean(tfidf_matrix.toarray(), axis=1)

        # Assign importance scores
        return {title: score * 100 for title, score in zip(self.titles, scores)}
