import requests
from bs4 import BeautifulSoup
import pandas as pd

# get data
URL = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,asc"
response = requests.get(URL)

# soupify it
soup = BeautifulSoup(response.text,'html.parser')

# find stuff we need
movie_release_dates = soup.findAll('span',class_ = 'lister-item-year text-muted unbold')

# create an empty list
list_rel_dates = []

for str_date in movie_release_dates:

    # fix stupid strings
    str_date = (str_date.text).replace("(", "")
    str_date = str_date.replace(")", "")
    str_date = str_date.replace("I","")
    str_date = str_date.strip()

    # change them into integers
    int_date = int(str_date)

    # append to our empty list
    list_rel_dates.append(int_date)
    
# make a pd.Series of our list, with a proper name of the column
rel_dated_series = pd.Series(list_rel_dates, name="Release date")

# now u can print it or do whatever. :)