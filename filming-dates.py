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


# # Filming Dates ###

# In[6]:


movie_hrefs = []
for soup in soups:
    movie_hrefs += soup.find_all('h3', class_='lister-item-header')

movie_hrefs_list = []
for mv_hrf in movie_hrefs:
    movie_hrefs_list.append( mv_hrf.contents[3]['href'] )

movie_hrefs_list

