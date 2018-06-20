import bs4
import csv
import requests
import codecs


def language_type(line):
    maxchar = max(line)
    if u'\u0900' <= maxchar <= u'\u097f':
        return 'hindi'
    return 'english'


res = requests.get('https://www.jagran.com/')
soup = bs4.BeautifulSoup(res.text, 'lxml')
hindi_news = []
for ul in soup.find_all('ul', attrs={'class': "commonList"}):
    for a in ul.find_all('a'):
        line = a.text
        if len(line) > 0 and language_type(line) == 'hindi':
            hindi_news.append(a.text + "\n")

with open('News.csv', mode='a', encoding='utf-8') as writeFile:
    writeFile.writelines(hindi_news)
