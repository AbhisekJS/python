import bs4
import requests
res =requests.get('https://en.wikipedia.org/wiki/Mahatma_Gandhi')
soup= bs4.BeautifulSoup(res.text,'lxml')
type(soup)
for i in soup.select('.toc'):
    print(i.text)
