import requests
from bs4 import BeautifulSoup
website_url = "https://www.imdb.com/search/title/?release_date=2010-01-01,2020-12-31&count=250"

res = requests.get(website_url)
soup = BeautifulSoup(res.text,'html.parser')
movies = soup.find_all("div",{"class":"lister-item-content"})
for movie in movies:
     title_element = movie.find ("a")
     title = title_element.text
     link = title_element["href"]
     print(title,link)