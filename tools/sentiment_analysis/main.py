from textblob import TextBlob
from newspaper import Article
import nltk

nltk.download('punkt')

url = 'https://en.wikipedia.org/wiki/Mathematics'
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
# print(text)

with open('myText.txt', 'r') as f:
    text = f.read()

blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)
