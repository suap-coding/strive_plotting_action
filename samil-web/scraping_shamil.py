import requests
import pandas as pd
from bs4 import BeautifulSoup

def frame_it(list_of_pd_series):
    return pd.concat(list_of_pd_series, axis=1)

URL_1_50     = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,asc"
URL_51_100   = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,asc&start=51&ref_=adv_nxt"

# create an empty list for release dates
list_rel_dates_1_50 = []
list_rel_dates51_100 = []

movie_runtime_1_50 = []
movie_runtime_51_100 = []

response_1_50 = requests.get(URL_1_50)
soup_1_50 = BeautifulSoup(response_1_50.text,'html.parser')
movie_release_dates_1_50 = soup_1_50.findAll('span',class_ = 'lister-item-year text-muted unbold')

response_51_100 = requests.get(URL_51_100)
soup_51_100 = BeautifulSoup(response_51_100.text,'html.parser')
movie_release_dates_51_100 = soup_51_100.findAll('span',class_ = 'lister-item-year text-muted unbold')

# 1-st part - processing
for str_date in movie_release_dates_1_50:
    # fix stupid strings
    str_date = (str_date.text).replace("(", "")
    str_date = str_date.replace(")", "")
    str_date = str_date.replace("I","")
    str_date = str_date.strip()

    # change them into integers
    int_date = int(str_date)

    # append to our empty list
    list_rel_dates_1_50.append(int_date)

for str_date in movie_release_dates_51_100:
    # fix stupid strings
    str_date = (str_date.text).replace("(", "")
    str_date = str_date.replace(")", "")
    str_date = str_date.replace("I","")
    str_date = str_date.strip()
    # change them into integers
    int_date1 = int(str_date)
    # append to our empty list
    list_rel_dates51_100.append(int_date1)

runtimes_1_50 = soup_1_50.findAll('span',class_ = "runtime")
runtimes_51_100 = soup_51_100.findAll('span',class_ = "runtime")

for runtime in runtimes_1_50:    
    movie_runtime_1_50.append(runtime.text)

for runtime in runtimes_51_100:    
    movie_runtime_51_100.append(runtime.text)
    
rel_dates_1_100 = list_rel_dates_1_50 + list_rel_dates51_100
rel_dates_series = pd.Series(rel_dates_1_100, name="Release Date")

runtimes_1_100 = movie_runtime_1_50 + movie_runtime_51_100
runtimes_series = pd.Series(runtimes_1_100, name="Runtime")


shamils_list = [rel_dates_series, runtimes_series]

df = frame_it(shamils_list)
print(df)