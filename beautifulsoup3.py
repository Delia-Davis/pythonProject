from bs4 import BeautifulSoup
import requests
source = requests.get('https://coreyms.com/').text
soup = BeautifulSoup(source, 'lxml')
article = soup.find('article')
print(article.prettify())
 vid_src = article.find('iframe', class_='youtube-player')[src]
 vid_id = vid_src.split('/',)[4]
 print(vid_id)