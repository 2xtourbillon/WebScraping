from bs4 import BeautifulSoup
import requests

url = 'https://news.ycombinator.com/newest'

response = requests.get(url)

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')
# print(soup.title)
articles = soup.find_all(name='a', class_='storylink')
for article in articles:
    # print(article.getText())
    pass


article_texts = []
article_links = []


for article in articles:
    text = article.getText()
    article_texts.append(text) # get text
    article_links.append(article.get('href')) #value of an attribute

article_upvotes = [int(vote.getText().split()[0]) for vote in soup.find_all(name='span', class_='score')]

print(*article_texts[:5], sep='\n', end='\n')
print(*article_links[:5], sep='\n', end='\n')
print(article_upvotes[:5], end='\n')

highest_index = article_upvotes.index(max(article_upvotes))
print('index:', highest_index)
print('article vote:', max(article_upvotes))
print('article text:', article_texts[highest_index])
print('article link:', article_links[highest_index])
