import requests
import bs4
res=requests.get('https://www.mysqltutorial.org/mysql-and/')
soup=bs4.BeautifulSoup(res.text,'lxml')

for link in soup.find_all('a',href=True):
    print(link['href'])