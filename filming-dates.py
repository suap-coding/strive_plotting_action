import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

responses = []
for position in range(1, 51, 50):
    request = requests.get(
        f"https://www.imdb.com/search/title/?title_type=feature&num_votes=10000,&countries=us&sort=user_rating,desc&start={position}"
    )
    responses.append(request)
print("Number of responses: ", len( responses))

soups = []
for response in responses:
    soups.append(BeautifulSoup(response.text, 'html.parser'))
print("Number of soups: ", len(soups))

### Filming Dates ###

movie_urls = []

# print(soups[0].find_all('a', href = True)[0]['href'])

# For reference:
# <a href="/title/tt0068646/?ref_=adv_li_tt">Der Pate</a>

# Searching for href values containing '/title/tt' gives
# 3 results for each movie (one for image, one for title 
# and one for votes. Last movie has 4 results for some 
# reason)


for a in soups[0].find_all('a', href = True):
    
    if "/title/tt" in a['href']:
        movie_urls.append(a['href'].strip('vote'))

# To drop duplicates
# Order will be lost however
movie_urls = list(set(movie_urls))

print(movie_urls)
print("Number of movie urls: ", len(movie_urls))