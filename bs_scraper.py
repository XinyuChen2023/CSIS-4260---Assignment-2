import requests
from bs4 import BeautifulSoup
import time

base_url = "https://www.nytimes.com/ca/section/technology?page="
articles = []
start_time = time.time()  # Start timer

for page in range(1, 20):  # Increase range to collect more articles
    url = base_url + str(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    for article in soup.find_all("article"):
        title = article.find("h3")
        link = article.find("a")

        if title and link:
            articles.append({"title": title.text.strip(), "link": link["href"]})

    if len(articles) >= 100:  # Stop when reaching 100 articles
        break

end_time = time.time()  # End timer
elapsed_time = end_time - start_time

# Print results
print(f"Total articles scraped: {len(articles)}")
print(f"Time taken: {elapsed_time:.2f} seconds")
