# necesary imports
import requests
import pandas as pd
from bs4 import BeautifulSoup

# framing function
def frame_it(list_of_pd_series):
    return pd.concat(list_of_pd_series, axis=1)

# data urls
URL_1_50     = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,asc"
URL_51_100   = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,asc&start=51&ref_=adv_nxt"

# responses
response_1_50 = requests.get(URL_1_50)
response_51_100 = requests.get(URL_51_100)

# soupify the responses
soup_1_50 = BeautifulSoup(response_1_50.text,'html.parser')
soup_51_100 = BeautifulSoup(response_51_100.text,'html.parser')


##### FIRST LETS DEAL WITH RELEASE DATES #####


# traverse the soup in search for the dates
movie_release_dates_1_50 = soup_1_50.findAll('span',class_ = 'lister-item-year text-muted unbold')
movie_release_dates_51_100 = soup_51_100.findAll('span',class_ = 'lister-item-year text-muted unbold')    


# create an empty list for release dates
list_rel_dates_1_50 = []
list_rel_dates51_100 = []

# process dates
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

# make them into pd.Series
rel_dates_1_100 = list_rel_dates_1_50 + list_rel_dates51_100
rel_dates_series = pd.Series(rel_dates_1_100, name="Release Date")


##### NOW THE RUNTIMES #####

# traverse the soup in search for runtimes
runtimes_1_50 = soup_1_50.findAll('span',class_ = "runtime")
runtimes_51_100 = soup_51_100.findAll('span',class_ = "runtime")

# create empty lists for runtimes
movie_runtime_1_50 = []
movie_runtime_51_100 = []

# process runtimes
for runtime in runtimes_1_50:    
    movie_runtime_1_50.append(runtime.text)
for runtime in runtimes_51_100:    
    movie_runtime_51_100.append(runtime.text)

# make them into pd.Series
runtimes_1_100 = movie_runtime_1_50 + movie_runtime_51_100
runtimes_series = pd.Series(runtimes_1_100, name="Runtime")


# profit
shamils_list = [rel_dates_series, runtimes_series]
df = frame_it(shamils_list)
print(df)