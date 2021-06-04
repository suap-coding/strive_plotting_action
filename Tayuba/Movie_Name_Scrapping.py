from bs4 import BeautifulSoup
import requests
import pandas as pd

movies1_50 = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,asc"
movies51_100 = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,asc&start=51&ref_=adv_nxt"
response = requests.get(movies1_50)
soup = BeautifulSoup(response.content, "html.parser")

# travers through the soup
names_soup = soup.find_all(name="h3")
# print(names_soup)

# create a list
names_list = []

# fill it with first 50
for idx in range(0, len(names_soup)-1):
    names_list.append(list(names_soup[idx])[3].text)


movies51_100 = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,asc&start=51&ref_=adv_nxt"
response = requests.get(movies51_100)
soup = BeautifulSoup(response.content, "html.parser")

# travers through the soup
names_soup = soup.find_all(name="h3")
# print(names_soup)

# append the next 50
for idx in range(0, len(names_soup)-1):
    names_list.append(list(names_soup[idx])[3].text)
# print(names_list)

names_series = pd.Series(names_list, name="Movie name")
# print(names_series)

names_of_genre = []


movie_types_soup = soup.find_all(name="span", class_="genre")

for idx1 in range(0, len(movie_types_soup)- 1):
    string = list(movie_types_soup[idx1])[0]
    names_of_genre.append(string)

# # print(names_of_genre)
movie_types_series = pd.Series(names_of_genre, name="Genre")
print(movie_types_series)

