import requests
from bs4 import BeautifulSoup


year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
URL = "https://www.billboard.com/charts/hot-100/"+year

top_songs = requests.get(URL).text

soup = BeautifulSoup(top_songs, 'html.parser')

songs = soup.find_all(name="h3", class_="a-no-trucate")

top_hundred = [song.string.strip() for song in songs]
print(len(top_hundred))



